class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Removed {product_name} from cart.")
                return
        print(f"{product_name} not found in cart.")

    def view_cart(self):
        print("Shopping Cart:")
        for product in self.products:
            print(f"  {product.name} - ${product.price} x {product.quantity}")

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total

    def checkout(self):
        total = self.calculate_total()
        print(f"Total: ${total:.2f}")
        print("Thank you for shopping!")

def main():
    cart = ShoppingCart()

    while True:
        print("1. Add product to cart")
        print("2. Remove product from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            cart.add_product(product)
        elif choice == "2":
            product_name = input("Enter product name to remove: ")
            cart.remove_product(product_name)
        elif choice == "3":
            cart.view_cart()
        elif choice == "4":
            cart.checkout()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()