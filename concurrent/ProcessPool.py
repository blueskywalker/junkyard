from multiprocessing import Pool


def hello(arg):
    print('Hello {}'.format(arg))


if __name__ == '__main__':

    pool = Pool(8)
    for i in range(50):
        pool.apply_async(hello, (i,))

    pool.close()
    pool.join()
