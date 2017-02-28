#!/usr/bin/env python
""" power set """

def comb(src):
    """ combination """
    stack = [[]]

    for item in src:
        size = len(stack)
        for index in range(size):
            stack.append(stack[index] + [item])

    return stack


def list_powerset(lst):
    result = [[]]
    for x in lst:
        result.extend([subset + [x] for subset in result])
    return result

def list_powerset2(lst):
    return reduce(lambda result, x : result + [subset + [x] for subset in result], lst, [[]])

def frozen_powerset(lst):
    return frozenset(map(frozenset, list_powerset(list(s))))


from pprint import pprint as pp
from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))


def bit_powerset(lst):

    n = len(lst)
    f = "{:0%db}" % (n,)

    def to_tuple(bpt):
        return tuple([ lst[i] for i in range(len(bpt)) if bpt[i]=='1'])

    return [to_tuple(f.format(i)) for i in range(2**n) ]


from pprint import pprint as pp
print comb(['a', 'b', 'c'])
pp(set(powerset({1,2,3,4})))
pp (bit_powerset(['a','b','c']))
