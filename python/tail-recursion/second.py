
def fact(n, r=1):
    if n < 1:
        return r
    return fact(n-1, n*r)  ## tail-recursion

if __name__ == '__main__':
    import sys

    print(fact(int(sys.argv[1])))