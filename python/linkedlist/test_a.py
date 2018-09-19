#!/usr/bin/env python3
from lru import LRUCache, lru_cache

import random

test= [ random.randint(1, 20) for _ in range(30) ]

cache = LRUCache(max_size=12)

# for item in test:
#     print(cache.get(data=item))

cache.show()

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def fib2(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

import timeit

def fib_test(func):
    data = [func(n) for n in range(1, 1000) ]
    #print(data)

print(timeit.timeit( 'fib_test(fib)' , globals=globals(), number=10))
print(timeit.timeit( 'fib_test(fib2)' ,globals=globals(), number=10))
