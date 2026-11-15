class Test:
    def m1(self):
        a=100
        print(a)

    def m2(self):
        b=200
        print(b)
        print(a)

t = Test()
t.m1()
t.m2()