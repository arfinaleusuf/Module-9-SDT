# Customar
# Employee
# Admin

from abc import ABC

class User(ABC):
    def __init__(self, name, phone,email, address):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class Empolyee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

# emp = Empolyee("rohim", "rohim@gmail.com", 12544846, "Dhaka", 23, "chef", 12000)
# print(emp.name)

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = [] # eta hocche amader database

    def add_employee(self,name, email, phone, address, age, designation, salary):
        #Employee class er ekta object toiri hoye jabe
        empoloyee = Empolyee(name, email, phone,address, age, designation, salary)
        self.employees.append(empoloyee)
        print(f"{name} is added!!")

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)

ad = Admin("korim", "14196565", "korim@gmail.com", "Dhaka")
ad.add_employee("Shagor", "s@gmail.com", "5644954", "khulna", 32, "chef", 12000)


ad.view_employee()