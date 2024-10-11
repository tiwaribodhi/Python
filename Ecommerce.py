class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []

    def __str__(self):
        return f"Username: {self.username}, \nPassword: {self.password}"

    def add_to_cart(self, product):
        self.cart.append(product)

    def remove_to_cart(self, product_name):
        for item in self.cart:
            if item[0] == product_name:
                self.cart.remove(item)
                print(f"Removed {product_name} from the cart.")
                return
        print(f"{product_name} not found in the cart.")

    def view_cart(self):
        return self.cart
    
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def update_stock(self, amount):
        self.stock += amount
        
class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product):
        if product.is_available():
            self.items[product.name] = product
          
    def remove_item(self, product):
        if product.name in self.items:
            del self.items[product.name] 

    def view_items(self):
        return self.items.values()
    
class Order:
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart
        self.status = "Pending"

    def place_order(self):
        return  "order placed"

    def view_order_details(self):
        return {
            "user": self.user.username,
            "status": self.status
        }
        
def main():
 username = input("enter username: ")
 password = input("enter password: ")
 user = User(username, password)
 print(user)

 print()

 print("Here is product list: ")
 product1 = Product("laptop", 50000, 100)
 product2 = Product("mobile", 10000, 90)
 product3 = Product("speaker", 5000, 50)
 product4 = Product("headphones", 3000, 80)
 product5 = Product("smartwatch", 15000, 60)
 product6 = Product("tablet", 20000, 40)
 product7 = Product("camera", 25000, 70)
 product8 = Product("keyboard", 2000, 120)
 product9 = Product("mouse", 1000, 150)
 product10 = Product("monitor", 15000, 30)

 cart = Cart()
 cart.add_item(product1)
 cart.add_item(product2)
 cart.add_item(product3)
 cart.add_item(product4)
 cart.add_item(product5)
 cart.add_item(product6)
 cart.add_item(product7)
 cart.add_item(product8)
 cart.add_item(product9)
 cart.add_item(product10)
 
 items = cart.view_items()
 print(f"{'Product Name':<15} {'Price (INR)':<15} {'Stock'}")
 print("-" * 45)
 for item in items:
        print(f"{item.name:<15} {item.price:<15} {item.stock}")
        
 user_choice_product = input("Enter product that you want: ")
 user_product_quantity = int(input("Enter pieces: "))
 com = input("you can only select one more do you want \nyes or no: ")
 def fetch_product_details(product, quantity, cart):
    if cart.items.get(product,None):
        if quantity <= cart.items[product].stock:
            print(f'(product : {product}, \nprice : {cart.items[product].price}, \ntotal price : {cart.items[product].price * quantity})')
            add = product, quantity, cart.items[product].price * quantity
            user.add_to_cart(add)#here
            i = user.view_cart()#here
            print(i)
        else:
            print(f"{quantity} are not available we only have {cart.items[product].stock}")
    else:
         print(f"Sorry! {user_choice_product} product is not available")
 
 if com == "yes":
     user_choice_product2 = input("Enter one more product that you want: ")
     user_product_quantity2 = int(input("Enter pieces: "))
     fetch_product_details(user_choice_product2, user_product_quantity2, cart)
     fetch_product_details(user_choice_product, user_product_quantity, cart)
 
 else:
     fetch_product_details(user_choice_product, user_product_quantity, cart)
     
 rem = input("1 for remove something, 2 for check product avalibility, 3 for place order: ")
 if rem == "1":
     q = input("product that you want to remove: ")
     user.remove_to_cart(q)
     i = user.view_cart()
     print(i)
 elif  rem == "2":
     pro = input("enter the product which availablity you want to check: ")
     if pro in cart.items:
        product = cart.items[pro]  # Get the existing product from the cart
        r = product.is_available()  # Check availability
        print(f"Product '{pro}' available: {r}")  # Print the availability status
     else:
        print(f"Product '{pro}' not found in the cart.")
 else:
     r = input("1 for placing order and 2 for view details: ")
     if r == "1":
         order = Order(user, cart); 
         r = order.place_order()
         print(r)
     else:
         order = Order(user, cart)
         r = order.view_order_details()
         print(r)
         r = input("1 for placing order and 2 for view details: ")
     if r == "1":
         order = Order(user, cart); 
         r = order.place_order()
         print(r)
         
 
 
 
if __name__ == "__main__":
  main()