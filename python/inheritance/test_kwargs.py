
def test_args(*args, **kwargs):
    for item in args:
        print(item)

    print(kwargs)
    for k, v in kwargs.items():
        print( k, v)

def testa(name, *args, **kwargs):
    print(name)
    test_args(*args,**kwargs)




testa('hello', 1 , 2 ,3, good='bad', babo='chunchi')


