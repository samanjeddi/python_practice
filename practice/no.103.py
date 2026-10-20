class Employee:

    salary = 3000

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return (f"{self.first_name + ' ' + self.last_name}")

a = input("First name: ")
b = input("Last name: ")

Employee1 = Employee(a, b)

print("Full name:", Employee1.get_full_name())
print("Salary: $",Employee1.salary)