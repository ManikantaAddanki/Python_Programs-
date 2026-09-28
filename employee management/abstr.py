from abc import ABC, abstractmethod


# ============================================================
# ABSTRACT CLASS: PRODUCT
# ============================================================

class Product(ABC):

    def __init__(self, product_id, name, price):
        self.__id = product_id
        self.__name = name
        self.__price = price

    # Getters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    # Abstract method
    @abstractmethod
    def display_details(self):
        pass


# ============================================================
# PHYSICAL PRODUCT
# ============================================================

class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, weight):
        super().__init__(product_id, name, price)
        self.weight = weight

    def display_details(self):
        print("Product Type :", "Physical Product")
        print("ID           :", self.get_id())
        print("Name         :", self.get_name())
        print("Price        : ₹", self.get_price())
        print("Weight       :", self.weight, "kg")


# ============================================================
# DIGITAL PRODUCT
# ============================================================

class DigitalProduct(Product):

    def __init__(self, product_id, name, price, file_size):
        super().__init__(product_id, name, price)
        self.file_size = file_size

    def display_details(self):
        print("Product Type :", "Digital Product")
        print("ID           :", self.get_id())
        print("Name         :", self.get_name())
        print("Price        : ₹", self.get_price())
        print("File Size    :", self.file_size, "MB")


# ============================================================
# CUSTOMER CLASS
# ============================================================

class Customer:

    def __init__(self, customer_id, name, email, password):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.__password = password

    # Registration
    def register(self):
        print("\nCustomer Registration Successful!")
        print("Customer Name :", self.name)
        print("Email         :", self.email)

    # Login
    def login(self, email, password):

        if self.email == email and self.__password == password:
            print("\nLogin Successful!")
            print("Welcome", self.name)
            return True

        print("\nInvalid email or password")
        return False


# ============================================================
# CART CLASS
# ============================================================

class Cart:

    def __init__(self):
        self.products = []

    # Add product
    def add_product(self, product):

        self.products.append(product)

        print(
            product.get_name(),
            "added to cart."
        )

    # Remove product
    def remove_product(self, product_id):

        for product in self.products:

            if product.get_id() == product_id:

                self.products.remove(product)

                print(
                    product.get_name(),
                    "removed from cart."
                )

                return

        print("Product not found in cart.")

    # List products
    def list_items(self):

        if not self.products:
            print("Cart is empty.")
            return

        print("\n========== CART ITEMS ==========")

        for product in self.products:

            print(
                "ID:",
                product.get_id(),
                "| Name:",
                product.get_name(),
                "| Price: ₹",
                product.get_price()
            )

    # Calculate total
    def calculate_total(self):

        total = 0

        for product in self.products:
            total += product.get_price()

        return total


# ============================================================
# ABSTRACT PAYMENT CLASS
# ============================================================

class Payment(ABC):

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process(self):
        pass


# ============================================================
# CREDIT CARD PAYMENT
# ============================================================

class CreditCardPayment(Payment):

    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def process(self):

        last_four = self.card_number[-4:]

        print("\nProcessing Credit Card Payment...")
        print("Amount :", self.amount)
        print("Card ending with : ****", last_four)
        print("Credit Card Payment Successful!")


# ============================================================
# PAYPAL PAYMENT
# ============================================================

class PayPalPayment(Payment):

    def __init__(self, amount, email):
        super().__init__(amount)
        self.email = email

    def process(self):

        print("\nProcessing PayPal Payment...")
        print("PayPal Email :", self.email)
        print("Amount :", self.amount)
        print("PayPal Payment Successful!")


# ============================================================
# ORDER CLASS
# ============================================================

class Order:

    def __init__(self, order_id, customer, cart, payment):

        self.order_id = order_id
        self.customer = customer
        self.cart = cart
        self.payment = payment

    # Place order
    def place_order(self):

        print("\n========== PLACING ORDER ==========")

        self.payment.process()

        print("\nOrder placed successfully!")
        print("Order ID :", self.order_id)

    # Display order
    def display_order_details(self):

        print("\n======================================")
        print("           ORDER DETAILS")
        print("======================================")

        print("Order ID       :", self.order_id)
        print("Customer ID    :", self.customer.customer_id)
        print("Customer Name  :", self.customer.name)
        print("Customer Email :", self.customer.email)

        print("\nProducts:")

        for product in self.cart.products:

            print(
                "-",
                product.get_name(),
                ": ₹",
                product.get_price()
            )

        print("--------------------------------------")

        print(
            "Total Amount   : ₹",
            self.cart.calculate_total()
        )

        print("======================================")


# ============================================================
# ADMIN CLASS
# ============================================================

class Admin:

    # Shared product catalog
    product_catalog = []

    def __init__(self, admin_name):
        self.admin_name = admin_name

    # Add product
    def add_product(self, product):

        Admin.product_catalog.append(product)

        print(
            "\nAdmin",
            self.admin_name,
            "added product:",
            product.get_name()
        )

    # Update product
    def update_product(
        self,
        product_id,
        new_name,
        new_price
    ):

        for product in Admin.product_catalog:

            if product.get_id() == product_id:

                product.set_name(new_name)
                product.set_price(new_price)

                print(
                    "Product updated successfully."
                )

                return

        print("Product not found.")

    # Delete product
    def delete_product(self, product_id):

        for product in Admin.product_catalog:

            if product.get_id() == product_id:

                Admin.product_catalog.remove(product)

                print(
                    "Product deleted successfully."
                )

                return

        print("Product not found.")

    # Display catalog
    @staticmethod
    def display_catalog():

        print("\n========== PRODUCT CATALOG ==========")

        if not Admin.product_catalog:
            print("No products available.")
            return

        for product in Admin.product_catalog:

            product.display_details()

            print("----------------------------------")


# ============================================================
# MAIN PROGRAM
# ============================================================

print("==========================================")
print("          E-COMMERCE OOP SYSTEM")
print("==========================================")


# ------------------------------------------------------------
# 1. CREATE ADMIN
# ------------------------------------------------------------

admin = Admin("Admin")


# ------------------------------------------------------------
# 2. CREATE PRODUCTS
# ------------------------------------------------------------

laptop = PhysicalProduct(
    101,
    "HP Laptop",
    65000,
    2.1
)

mobile = PhysicalProduct(
    102,
    "Samsung Mobile",
    30000,
    0.5
)

course = DigitalProduct(
    103,
    "Java Programming Course",
    1999,
    850
)


# ------------------------------------------------------------
# 3. ADD PRODUCTS TO CATALOG
# ------------------------------------------------------------

admin.add_product(laptop)
admin.add_product(mobile)
admin.add_product(course)


# Display catalog
Admin.display_catalog()


# ------------------------------------------------------------
# 4. UPDATE PRODUCT
# ------------------------------------------------------------

print("\nUpdating Mobile...")

admin.update_product(
    102,
    "Samsung Galaxy Mobile",
    28000
)

Admin.display_catalog()


# ------------------------------------------------------------
# 5. CUSTOMER REGISTRATION
# ------------------------------------------------------------

customer = Customer(
    501,
    "Manikanta",
    "manikanta@gmail.com",
    "12345"
)

customer.register()


# ------------------------------------------------------------
# 6. CUSTOMER LOGIN
# ------------------------------------------------------------

customer.login(
    "manikanta@gmail.com",
    "12345"
)


# ------------------------------------------------------------
# 7. CREATE CART
# ------------------------------------------------------------

cart = Cart()


# Add products
cart.add_product(laptop)
cart.add_product(mobile)
cart.add_product(course)


# Display cart
cart.list_items()


# ------------------------------------------------------------
# 8. REMOVE PRODUCT
# ------------------------------------------------------------

print("\nRemoving Mobile from Cart...")

cart.remove_product(102)

cart.list_items()


# ------------------------------------------------------------
# 9. CALCULATE TOTAL
# ------------------------------------------------------------

total = cart.calculate_total()

print("\nCart Total : ₹", total)


# ------------------------------------------------------------
# 10. PAYMENT
# ------------------------------------------------------------

payment = CreditCardPayment(
    total,
    "1234567890123456"
)


# ------------------------------------------------------------
# 11. CREATE ORDER
# ------------------------------------------------------------

order = Order(
    1001,
    customer,
    cart,
    payment
)


# ------------------------------------------------------------
# 12. PLACE ORDER
# ------------------------------------------------------------

order.place_order()


# ------------------------------------------------------------
# 13. DISPLAY ORDER
# ------------------------------------------------------------

order.display_order_details()


# ------------------------------------------------------------
# 14. DELETE PRODUCT
# ------------------------------------------------------------

print("\nDeleting Java Programming Course...")

admin.delete_product(103)

Admin.display_catalog()


print("\n========== PROGRAM COMPLETED ==========")