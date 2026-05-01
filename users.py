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
        self.cart = Order()
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item Quantity Exceeded!!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("item added")
        else:
            print('item not found')
            
    def view_cart(self):
        print("***View Cart***")
        print("Name\tprice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price} {item.quantity}")
        print(f"total price: {self.cart.total_price}")

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

class Order:
    def __init__(self):
        self.items = {}
    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity  # jodi item ta cart e already thake
        else:
            self.items[item] = item.quantity  # cart e item jodi na thake

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    
    def clear(self):
        self.items = {}


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

mamar_res = Restaurent("Mamar Restaurent")
mn = Menu()
item = FoodItem("pizza", 12.25, 10)
item2 = FoodItem("Burger", 10, 30)
admin = Admin("Rohin","rahim@gmail.com", 6546432, "Dhaka")
admin.add_new_item(mamar_res,item)
admin.add_new_item(mamar_res,item2)

customer1 = Customer("Rohin","rahim@gmail.com", 6546432, "Dhaka")
customer1.view_menu(mamar_res)

item_name = input("enter item name: ")
item_quantity = int(input("Enter Item Quantity: "))

customer1.add_to_cart(mamar_res, item_name, item_quantity)
customer1.view_cart()