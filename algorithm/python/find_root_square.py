#!/usr/bin/env python
""" SQUARE ROOT """
from __future__ import division


def babylonian(n):
    """ Babylonian """

    guess = n / 2

    def diff_from_origin(v):
        return abs(v**2 - n)

    while diff_from_origin(guess) > 0.0000001:
        tmp = n / guess
        guess = (tmp + guess) / 2

    return guess

print( babylonian(2) )
print( babylonian(20) )
