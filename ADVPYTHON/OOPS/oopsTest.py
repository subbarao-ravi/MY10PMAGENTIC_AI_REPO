class Employee:
    def __init__(self,empno,empname,sal):
        self.empno=empno
        self.empname=empname
        self.sal=sal

    def display(self):
        print('empno ',self.empno)
        print('empname ',self.empname)
        print('sal ',self.sal)


class Test:
    
    def modify(emp):
        emp.sal = emp.sal+10000
        emp.display()

e = Employee('ETPL255','SUBBARAO',60000)
Test.modify(e)

