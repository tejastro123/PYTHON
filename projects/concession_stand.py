class ConcessionItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ConcessionStand:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                print(f"Removed {item_name} from concession stand.")
                return
        print(f"{item_name} not found in concession stand.")

    def view_inventory(self):
        print("Concession Stand Inventory:")
        for item in self.items:
            print(f"  {item.name} - ${item.price} x {item.quantity}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def make_sale(self, item_name, quantity):
        for item in self.items:
            if item.name == item_name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    print(f"Sold {quantity} {item_name}(s).")
                    return
                else:
                    print(f"Not enough {item_name}(s) in stock.")
                    return
        print(f"{item_name} not found in concession stand.")

def main():
    stand = ConcessionStand()

    while True:
        print("1. Add item to concession stand")
        print("2. Remove item from concession stand")
        print("3. View inventory")
        print("4. Make a sale")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = ConcessionItem(name, price, quantity)
            stand.add_item(item)
        elif choice == "2":
            item_name = input("Enter item name to remove: ")
            stand.remove_item(item_name)
        elif choice == "3":
            stand.view_inventory()
        elif choice == "4":
            item_name = input("Enter item name to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            stand.make_sale(item_name, quantity)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()