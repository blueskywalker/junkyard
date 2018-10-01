
class TailCall(object) :
    def __init__(self, call, *args, **kwargs) :
        self.call = call
        self.args = args
        self.kwargs = kwargs
    def handle(self) :
        return self.call(*self.args, **self.kwargs)

def t(f) :
    def _f(*args, **kwargs) :
        ret = f(*args, **kwargs)
        while type(ret) is TailCall :
            ret = ret.handle()
        return ret
    return _f

@t
def fact(n, r=1) :
    if n <= 1 :
        return r
    else :
        return TailCall(fact, n-1, n*r)

if __name__ == '__main__':
    import sys

    print(fact(int(sys.argv[1])))

