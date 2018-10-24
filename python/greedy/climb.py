#!/usr/bin/env python3
import sys


lookup=dict()

lookup[0]=0
lookup[1]=1
lookup[2]=2

def climbsteps(n):
    if n in lookup:
        return lookup[n]

    answer = climbsteps(n-1) + climbsteps(n-2)

    lookup[n] = answer
    return answer


print(climbsteps(int(sys.argv[1])))

