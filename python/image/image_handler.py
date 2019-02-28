
import cv2
import numpy as np
import os
import struct
from .nio_thread_pool import ProcessPool
import logging
import glob


def create_directories(dirs):
    for target in dirs:
        if not os.path.exists(target):
            os.makedirs(target)


def compress_bit_depth(raw_img, orig_depth, new_depth):
    raw_img = raw_img * float(2 ** new_depth - 1) / (2 ** orig_depth - 1)
    raw_img = raw_img.round().astype(np.uint8)
    return raw_img


def apply_LUT(raw_img, w, h, lut_table):
    for i in range(h):
        for j in range(w):
            px = raw_img.item(i, j)
            lut_val = lut_table[px]
            raw_img.itemset((i, j), lut_val)
    return raw_img


def extract_red_channel_image(red_dir, raw_img, imagefilename):
    red_img = raw_img[::2, ::2]
    # store the red channel image
    output_name = imagefilename + ".png"
    output_path = os.path.join(red_dir, output_name)
    cv2.imwrite(output_path, red_img)


def demosaic_raw_image(gray_dir, raw_img, imagefilename):
    img = cv2.cvtColor(raw_img, cv2.COLOR_BayerGR2GRAY)
    # store the grayscale image
    output_name = imagefilename + ".png"
    output_path = os.path.join(gray_dir, output_name)
    cv2.imwrite(output_path, img)


def convert_image(file_path,gray_dir, red_dir, h_target="vdiHeight", w_target="vdiWidth",
                   img_target="65535", lut_target="lookupTable"):
    logger = logging.getLogger('mobileye')
    logger.info('IMAGE PROCESS - {}'.format(file_path))

    dirname, filename = os.path.split(file_path)
    imagefilename = filename.replace(".pgm", "")
    # for each pgm file, do the color correction and export to the appropriate directory on disk
    with open(file_path, 'rb') as f:
        count = 0
        while (True):
            # read one line at a time
            line = f.readline().decode('ISO-8859-1')
            # Detect reading EOF
            if not line:
                break
            # Parse image information from header
            elif line.find(h_target) > 0:
                h = int(line.split('=')[1])
                # print(h)
            elif line.find(w_target) > 0:
                w = int(line.split('=')[1])
                # print(w)
            elif line.find(lut_target) > 0:
                lut_string = line.split('=')[1]
                lut_string = lut_string.replace('{', '').replace('}', '').replace(' ', '')
                lut_list = lut_string.split(',')
                lut_table = [int(i) for i in lut_list]
            elif line.startswith('#MicrosecTimeStamp'):
                ts = int(line.split('=')[1])
                imagefilename = "%s_%d" % (imagefilename, ts)

            if line.strip() != img_target:
                continue

            # Read 1 entire image
            # Parse 2 bytes per pixel with little endianness
            bytes = f.read(h * w * 2)
            unpack_fmt = '<' + str(h * w) + 'H'
            pixels = struct.unpack(unpack_fmt, bytes)
            # extract the raw image
            raw_img = np.flipud(np.asarray(pixels).astype(np.uint16).reshape((h, w)))

            # compress the 16-bit image to 8-bit depth
            # print("compressing the image depth to 8 bits")
            orig_depth, new_depth = 16, 8
            raw_img = compress_bit_depth(raw_img, orig_depth, new_depth)

            # Apply the LUT
            # print("apply the LUT")
            raw_img = apply_LUT(raw_img, w, h, lut_table)

            # Extract red channel pixels
            # print("extract the red channel image")
            extract_red_channel_image(red_dir, raw_img, imagefilename)

            # De-mosaicing kernel described here:
            # print("applying the demosaicing")
            demosaic_raw_image(gray_dir, raw_img, imagefilename)


def generating_low_resolution(resolution, path, dest):
    logger = logging.getLogger('mobileye')
    logger.info('LOW RESOLUTION PROCESS {resolution} : {path}'.format(**locals()))

    try:
        img = cv2.imread(path, flags=cv2.IMREAD_GRAYSCALE)
        h, w = img.shape
        aspect_ratio = float(h) / w
        width = resolution
        height = int(width * aspect_ratio)
        small_img = cv2.resize(img, (width, height))

        target = '/'.join([dest,path.split('/')[-1]])

        cv2.imwrite(target, small_img)
    except Exception as e:
        logger.error(e)


class ImageTransform(object):

    def __init__(self):
        self.no_process = os.getenv('MAX_PROCESS','10')
        self.thread_pool = ProcessPool(int(self.no_process))
        self.h_target = "vdiHeight"
        self.w_target = "vdiWidth"
        self.img_target = "65535"
        self.lut_target = "lookupTable"

    def add(self, path, output):
        gray_dir=os.path.join(output,'grayscale')
        red_dir=os.path.join(output, 'red')
        create_directories([gray_dir, red_dir])
        self.thread_pool.add_task(convert_image, path, gray_dir, red_dir, self.h_target, self.w_target, self.img_target, self.lut_target )

    def scan_and_execute(self, path, output):
        for pgm in glob.glob(os.path.join(path,'*.pgm')):
            self.add(pgm, output)

    def close(self):
        self.thread_pool.wait_completion()
        self.thread_pool.terminate()


class LowResolutionGenerator(object):

    def __init__(self, base_dir, dest_dir):
        self.no_process = os.getenv('MAX_PROCESS', '10')
        self.resolution = int(os.getenv('LOW_IMG_RESOLUTION', '800'))
        self.thread_pool = ProcessPool(int(self.no_process))
        self.base_dir = base_dir
        self.dest_dir = dest_dir

    def add(self, path, dest):
        self.thread_pool.add_task(generating_low_resolution, self.resolution, path, dest)

    def scan_and_execute(self):
        for png in glob.glob(os.path.join(self.base_dir, '**','*.png'), recursive=True):
            dirname, basename = os.path.split(png)
            subpath = dirname[len(self.base_dir):]
            if subpath.startswith('/'):
                subpath = subpath[1:]
            output_path = os.path.join(self.dest_dir, subpath)
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            self.add(png, output_path)

    def close(self):
        self.thread_pool.wait_completion()
        self.thread_pool.terminate()
