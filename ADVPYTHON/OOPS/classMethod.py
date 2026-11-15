class Animal:
    legs = 4
    @classmethod
    def walk(cls,name):
        print(name,"walks with ",cls.legs,' legs')

a=Animal()
a.walk('DOG')
a.walk('CAT')

class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1

    @classmethod
    def noOfObjectsCreated(cls):
        print("no of objects created ",cls.count)

t = Test()
t1= Test()
Test.noOfObjectsCreated()
t3=Test()
t4=Test()
t5=Test()
Test.noOfObjectsCreated()

