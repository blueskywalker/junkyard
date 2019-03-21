#!/usr/bin/env python

import glob2
import fileinput

sources=glob2.glob('/tmp/minutes/*txt')

with open('/tmp/ts.txt','w') as fout:
    for item in sources:
        with open(item) as infile:
            fout.write(infile.read()+'\n')
