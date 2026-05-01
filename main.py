from food_item import FoodItem
from menu import Menu
from users import Customer, Admin, Empolyee
from restaurant import Restaurent
from orders import Order


mamar_restuarent = Restaurent("Mamar_Restaurent")
def customer_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    adderss = input("Enter Your Address: ")
    customer = Customer(name = name, email = email, phone = phone, adderss = adderss)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add Item to cart")
        print("3. View cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter Your Choice"))
        if choice == 1:
            customer.view_menu(mamar_restuarent)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            item_quantity = int(input("Enter item Quantity"))
            customer.add_to_cart(mamar_restuarent, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Input")