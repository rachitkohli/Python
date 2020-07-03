class Employee:
    empCount = 0
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        Employee.empCount += 1
    
    def getDetails(self):
        return self.name + " == " + self.designation

class InheritEmployee(Employee):    #Inheriting Employee class
    def __init__(self):
        print ("InheritEmployee Initiate")
        Employee.empCount += 1

emp1 = Employee("Rachit", "Software Engineer")
emp2 = Employee("Nick", "Analyst")
print (emp1.getDetails())
print (emp2.getDetails())
print(Employee.empCount)

emp3 = InheritEmployee()
emp3.name = "Kishore"
emp3.designation = "Sales"
print (emp3.getDetails())
print(emp3.empCount)