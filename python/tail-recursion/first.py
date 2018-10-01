

def fact(n):
    if n < 1: return 1
    return n * fact(n-1) # not tail recursion



if __name__ == '__main__':
    import sys

    print(fact(int(sys.argv[1])))
    
