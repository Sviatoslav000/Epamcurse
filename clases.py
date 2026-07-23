class Employee:
    empCount=0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total Employee ",Employee.empCount)

    def displayEmployee(self):
        print("Name", self.name," Salary:", self.salary)

emp1 = Employee("Slave", 200)
emp2 = Employee("Master", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.displayCount()
emp2.displayCount()

print("Total emploee: ", Employee.empCount)

emp1.age=22

print(hasattr(emp1, 'age'))
print(getattr(emp1, "age"))

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()  # 1
counter.count()  # 2

print(counter._JustCounter__secretCount)   # 2
print(counter.__secretCount)  # AttributeError
