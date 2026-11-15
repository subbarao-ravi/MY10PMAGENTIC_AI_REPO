class Employee:
    companyName='Evergent Technologies Pvt Ltd'
    def __init__(self,name,empId):
        self.empname=name
        self.empId=empId
        Employee.department='JAVA'

    def empDetails(self):
        print('empname',self.empname)
        print('empId',self.empId)
        print('companyName',self.companyName)
        Employee.work='DEVELOPMENT'

    @staticmethod
    def billingName():
        Employee.billingname='SOHINI TECH PARK'

    @classmethod
    def workPlace(cls):
        cls.officeAddress='NANAKRAM GUDA'
        Employee.officeFloor=11


print(Employee.__dict__)
e=Employee('Subbarao','ETPL255')
print(Employee.__dict__)
e.empDetails()
print(Employee.__dict__)
Employee.billingName()
print(Employee.__dict__)
Employee.workPlace()
print(Employee.__dict__)
Employee.colleague='RAMA'
print(Employee.__dict__)


