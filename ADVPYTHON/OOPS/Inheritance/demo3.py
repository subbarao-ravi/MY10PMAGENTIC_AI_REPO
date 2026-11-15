class P:
    a=10
    def __init__(self):
        print('parent constructor called')
        self.b=100

    def m1(self):
        pass

class C(P):
    def __init__(self):
        super().__init__()cd

c = C()
c.a
c.b
c.m1()