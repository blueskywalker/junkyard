#!/usr/bin/env python

from datetime import datetime
import re

START='2017-08-31T10:00:00Z'

def parse_iso8601(input_date):
    return datetime(*map(int, re.split('[^\d]',input_date)[:-1]))

def get_timestamp(dt):
    return (dt - datetime(1970,1,1)).total_seconds()


print get_timestamp(parse_iso8601(START))

