class Test:

    @staticmethod
    def add(x,y):
        print("(x+y)",x+y)

    @staticmethod
    def mul(x,y):
        print("(x*y)",x*y)

    def div(x,y):
        print("(x+y)/2", (x+y)/2)



Test.add(4,3)
Test.mul(5,7)
t = Test()
t.add(2,3)
t.mul(5,6)
t.div(4,3)

