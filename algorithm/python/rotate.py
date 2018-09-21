#!/usr/bin/env python

import sys

n=7
k=4
q=4

src=[i for i in range(1,n+1)]
k-=1
result = src[k:] + src[:k]

print result


