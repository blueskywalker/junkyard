#!/usr/bin/env python

import sys
import time

for line in sys.stdin:
    print time.ctime(int(line.strip())/1000000000)

