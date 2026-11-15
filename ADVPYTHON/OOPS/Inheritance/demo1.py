class Engine:
    a=10
    def __init__(self):
        self.b=20

    def m1(self):
        print('engine specific methods')


class Car:
    def __init__(self):
        self.c=30
        self.engine=Engine()

    def display(self):
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()

c = Car()
c.display()
