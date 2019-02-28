

class Base(object):
    def __init__(self):
        print("base")


class childA(Base):

    def __init__(self,a):
        super(childA, self).__init__()
        print(a)

class childB(childA):

    def __init__(self):
        super(childB, self).__init__( 'good')


child=childB()
