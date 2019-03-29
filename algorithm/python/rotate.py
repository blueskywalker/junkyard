#!/usr/bin/env python

import sys

n=11
k=8


src=[i for i in range(1,n+1)]
k-=1
result = src[k:] + src[:k]

print( result )

def find_rotate(alist):
    first = 0
    last = len(alist)-1

    while first < (last-1):
        mid = (first + last) // 2

        if alist[first] < alist[mid]:
            first = mid

        if alist[mid] < alist[last]:
            last = mid

    return last

print(find_rotate(result))
