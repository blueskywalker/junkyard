
from __future__ import print_function

class test(object):
    a=1
    b=2

    def __init__(self):
        print("init")

    def describe(self):
        print(self.a,self.b)



t=test()
t.describe()
