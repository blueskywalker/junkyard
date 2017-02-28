#!/usr/bin/env python
""" integerize """
import math

def integerize(src):
    """ integerize """
    all_cases = []
    total = sum(map(round,src))

    def _all_cases(src, depth, trace):
        if len(src) == depth:
            all_cases.append(trace)
            return

        _all_cases(src, depth + 1, trace + [int(math.floor(src[depth]))])
        _all_cases(src, depth + 1, trace + [int(math.ceil(src[depth]))])

    def find_min_diff():
        'find minum diff'
        def calc_diff(candidate):
            """ calc diff """
            return sum([float(abs(candidate[i] - src[i])) / src[i] for i, _ in enumerate(candidate)])

        matched_candidate = filter(lambda x: x[1]!=total ,[(i, calc_diff(c)) for i, c in enumerate(all_cases)] )
#        print matched_candidate
        minmumal = min(matched_candidate, key=lambda x: x[1])
        return all_cases[minmumal[0]]

    _all_cases(src, 0, [])
    return find_min_diff()


source = [1.2, 3.6, 2.2, 1.9, 2.2]
print source
print sum(map(round,source))
minvalue = integerize(source)
print minvalue
print sum(minvalue)
