# Online Python Compiler.
# Code, Compile, Run and Debug python program online.
# Write your code in this editor and press "Run" button to execute it.

print("Hello World")

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        print(f"Added {menu_item.name} to order.")

    def show_order(self):
        if not self.items:
            print("Your order is empty.")
            return
        print("\nYour current order:")
        total = 0
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item}")
            total += item.price
        print(f"Total: ${total:.2f}")

def show_menu(menu):
    print("\nMenu:")
    for idx, item in enumerate(menu, start=1):
        print(f"{idx}. {item}")

def main():
    menu = [
        MenuItem("Burger", 5.99),
        MenuItem("Pizza", 8.49),
        MenuItem("Salad", 4.25),
        MenuItem("Soda", 1.50)
    ]

    order = Order()

    while True:
        print("\nWhat would you like to do?")
        print("1. Show Menu")
        print("2. Add Item to Order")
        print("3. Show Current Order")
        print("4. Checkout & Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_menu(menu)
        elif choice == '2':
            show_menu(menu)
            try:
                item_choice = int(input("Enter item number to add: "))
                if 1 <= item_choice <= len(menu):
                    order.add_item(menu[item_choice - 1])
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a number.")
        elif choice == '3':
            order.show_order()
        elif choice == '4':
            print("\nFinal Order:")
            order.show_order()
            print("Thank you! See you next time.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
