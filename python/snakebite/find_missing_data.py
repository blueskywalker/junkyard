#!/usr/bin/env python

import pytz
from datetime import datetime
import sys
import os

PREFIX='/data/hub/vehicle/MKZ-Grey'

with open('sortedTS.txt') as f:
    for line in f:
        dt = datetime.utcfromtimestamp(int(line[:10]))
        directory = os.path.join(PREFIX, "%04d/%02d/%02d/%02d/%02d/%02d/%s" %(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second,line.strip()))
        print directory
        sys.exit(1)

