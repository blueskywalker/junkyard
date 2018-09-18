
import functools

@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)



data = [ fib(n) for n in range(1, 30) ]
print(data)

