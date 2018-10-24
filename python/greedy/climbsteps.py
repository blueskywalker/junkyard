#!/usr/bin/env python3
import sys

class CounterSteps(object):
    def __init__(self):
        self.count=0

    def climbsteps(self, n, trace):
        if n < 1:
            return

        if n < 2:
            trace.append(1)
            #print(trace)
            self.count+=1
            return

        self.climbsteps(n-1, trace + [1])

        if n < 3:
            trace.append(2)
            #print(trace)
            self.count+=1
            return

        self.climbsteps(n-2, trace + [2])


def climbsteps(n):
    cs = CounterSteps()
    cs.climbsteps(n, [])
    return cs.count



