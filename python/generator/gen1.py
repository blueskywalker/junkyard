#!/usr/bin/env python

def genN(n):
    i=0
    while i < n:
        yield i
        i += 1

def first(g):
    value = None
    try:
        value = g.next()
    except:
        pass
    return value

def last(g):
    value=None
    try:
        while True:
            value=g.next()
    except Exception as e:
        pass
    return value

g = genN(0)

print(g)
print(first(g))
print(last(g))

