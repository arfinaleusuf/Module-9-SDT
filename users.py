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

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = None
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    def add_to_cart(self, restaurent, item_name):
        item = restaurent.menu.find_item(item_name)
        if item:
            pass
        else:
            print('item not found')

    def view_cart(self):
        print("***View Cart***")
        print("Name\tprice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name} {item.price} {item.quantity}")
        print("total price: {self.cart.total_price}")



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


    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_items(item)

    def delete_item(self, restaurant, item):
        restaurant.menu.remove_item(item)

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # eta hocche amader database
        self.menu = FoodItem()
    
    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name, emp.email, emp.phone, emp.address)


class Menu:
    def __init__(self):
        self.items = [] #items er database

    def add_menu_items(self, item):
        self.items.append(item)
        
    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item_name
        return None
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted")
        else:
            print("Item not found")

    def show_menu(self):
        print("***** Menu *****")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


mn = Menu()
item = FoodItem("pizza", 12.25, 10)
mn.add_menu_items(item)
mn.show_menu()