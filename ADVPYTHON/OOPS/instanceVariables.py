class Student:
    ''' This is Student class'''
    def __init__(self,name,age,marks):
        self.name=name
        self.marks=marks
        self.age=age

    def display(self):
        print('studnet details...')
        print('name',self.name)
        print('marks',self.marks)
        print('age',self.age)

    def setEName(self, name):
        self.name=name

    def getName(self):
        return self.name


#name=input('enter student name ')
#age=float(input('enter student age '))
#marks=float(input('enter stundent marks '))

s=Student('RAMA',25,100)
s.display()
s.address='Hyderabad'
s.age=16
del s.address
print(s.__dict__)

s1=Student('SUBBARAO',39,35)
s1.setEName('SIVA')
s1.address='Pulikonda'
print(s1.__dict__)