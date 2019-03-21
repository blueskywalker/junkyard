#!/usr/bin/env python

def genN(n):
    i=0
    while i < n:
        yield i
        i += 1

g=genN(10)

lst = list(g)
print lst[0], lst[-1]
