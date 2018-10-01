

class TailCaller(object) :
    def __init__(self, f) :
        self.f = f
    def __call__(self, *args, **kwargs) :
        ret = self.f(*args, **kwargs)
        while type(ret) is TailCall :
            ret = ret.handle()
        return ret


class TailCall(object) :
    def __init__(self, call, *args, **kwargs) :
        self.call = call
        self.args = args
        self.kwargs = kwargs
    def handle(self) :
        if type(self.call) is TailCaller:
            return self.call.f(*self.args, **self.kwargs)
        else:
            return self.call(*self.args, **self.kwargs)

def tailcall(f) :
    def _f(*args, **kwargs) :
        return TailCall(f, *args, **kwargs)
    return _f

@TailCaller
def fact(n, r=1) :
    if n <= 1 :
        return r
    else :
        return tailcall(fact)(n-1, n*r)

if __name__ == '__main__':
    import sys

    print(fact(int(sys.argv[1])))
