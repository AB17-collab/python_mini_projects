class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def getSalary(self):
        return self.salary


arnab = Employee("Arnab", 900000)
print(arnab.getSalary)
