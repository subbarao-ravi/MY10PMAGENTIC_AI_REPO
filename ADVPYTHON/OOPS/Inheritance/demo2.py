class Car:
    def __init__(self,name,color,model):
        self.name=name
        self.color = color
        self.model=model

    def getInfo(self):
        print("Car Name:{} , Model:{} and Color:{}".format(self.name,self.model,self.color)) 


class Employee:
    def __init__(self,name,eno,car):
        self.name=name
        self.eno=eno
        self.car = car

    def display(self):
        print("Employee Name:",self.name)
        print("Employee Number:",self.eno)  
        print("Employee Car Info:")
        self.car.getInfo()

c=Car("Innova","Grey","2.5V")
e=Employee('Durga',10000,c)   
e.display()
