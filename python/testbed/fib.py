#!/usr/bin/env python


def fib1(n):
    if n<3:
        return 1
    return fib(n-2) + fib(n-1)

def fib(n):

    if n < 1:
        return 0

    n1,n2 = 1, 1

    while n > 2:
        n1, n2 = n1+n2, n1
        n-=1

    return n1


def main():
    import sys
    if len(sys.argv) < 2:
        print 'need a number'
        sys.exit(1)

    print fib(int(sys.argv[1]))


if __name__ == "__main__":
    main()
