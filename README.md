E-Commerce System in Python 🛒
Project Overview
This project is an intermediate-level implementation of an e-commerce system developed in Python, using Object-Oriented Programming (OOP) concepts. It simulates essential functionalities of an e-commerce platform, including product management, cart operations, and order placement. The system interacts with users via the console to allow smooth handling of product availability, cart management, and order processing.

Key Features
User Account Management: Create and manage user profiles with unique usernames and passwords.
Product Inventory System: Define products with attributes such as name, price, and stock levels. Stock availability is dynamically updated.
Shopping Cart Operations: Add, remove, and view products in the cart. The system checks product availability before allowing the addition to the cart.
Order Placement: Users can place orders based on the items in their cart and view order details, including order status.
Stock Availability Check: Products have real-time stock checks to prevent ordering items that are out of stock.

Technologies Used
Python: The core programming language.
Object-Oriented Programming (OOP): Modular design with classes for User, Product, Cart, and Order.
CLI Interaction: Command-line interface for user inputs and outputs.

Project Structure
├── main.py            # Main script to run the e-commerce system
├── README.md          # Project documentation
└── requirements.txt   # (Optional) List of dependencies

Workflow
User Creation: The system prompts users to enter a username and password to create their profile.
Product Listing: Displays a list of available products with their name, price, and stock.
Adding to Cart: Users select products to add to their cart. The system checks stock before allowing products to be added.
Removing from Cart: Users can remove any product from their cart.
Checking Product Availability: Before adding a product, users can check if the desired quantity is available in stock.
Placing Orders: Once users are satisfied with the items in their cart, they can place an order and view order details.

Example of Usage
Login: The user is asked to enter a username and password to create their account.
View Product List: The available products are displayed along with their prices and stock.
Add Products: The user selects a product and specifies the quantity. If the stock is sufficient, the product is added to the cart.
Remove Products: Users can remove any unwanted items from their cart.
Place an Order: The user can finalize their cart and place the order. Order details, including the total price and status, are displayed.

Future Improvements
Database Integration: To store user profiles and products for persistence.
User Authentication: Add more secure login features.
Payment Gateway: Integrate a mock payment system to simulate real-world transactions
