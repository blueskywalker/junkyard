#!/usr/bin/env python3
from lru import LRUCache, lru_cache

import random

test= [ random.randint(1, 20) for _ in range(30) ]

cache = LRUCache(max_size=12)

# for item in test:
#     print(cache.get(data=item))

cache.show()

test_size=10
@lru_cache(max_size=test_size)
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
    data = [func(n) for n in range(1, test_size) ]
    print(data)

print(timeit.timeit( 'fib_test(fib)' , globals=globals(), number=5))
print(timeit.timeit( 'fib_test(fib2)' ,globals=globals(), number=5))
