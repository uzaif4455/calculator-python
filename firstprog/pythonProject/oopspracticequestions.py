#1) Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.
"""import math
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi* self.radius**2
    def perimeter(self):
        return 2* math.pi*self.radius
radius=int(input("enter the radius"))
circle=circle(radius)
area=circle.area()
perimeter=circle.perimeter()
print("the area of circle is :",area)
print("the perimeter of the circle is:",perimeter)"""
#2)Write a Python program to create a person class. Include attributes like name,
# country and date of birth.
# Implement a method to determine the person's age.
'''from datetime import date
class person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def calculate_age(self):
            today=date.today()
            age=today.year-self.dob.year
            if today < date(today.year,self.dob.month,self.dob.day):
                age-=1
            return age
person1=person("jack","us",date(1990,5,2))
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.dob)
print("Age:", person1.calculate_age())'''
#3)Write a Python program to create a calculator class. Include methods for basic arithmetic
# operations.
'''import math
class calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mult(self,a,b):
        return a*b
    def div(self,a,b):
        if b!=0:
            return a/b
        else:
            print("numerator can not be 0")
# a=int(input("enter the number : "))
# b=int(input("enter the number: "))
calculator=calculator()
add=calculator.add(5,4)
sub=calculator.sub(10,5)
mult=calculator.mult(22,10)
div=calculator.div(110,20)
print(" the addition of a and b is: ", add)
print("the subtration of a and b is :",sub)
print("the multipication of a and b is :",mult)
print("the division of a and b is :",div)'''
#4)Write a Python program to create a class that represents a shape.
# Include methods to calculate
# its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and square
'''import math
class shape:
     def calculate_area(self):
         pass
     def calculate_perimeter(self):
         pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius

    def calculate_area(self):
        return math.pi* radius**2
    def calculate_perimeter(self):
        return 2*math.pi*radius
class rectangle(shape):
    def calculate_area2(self,l,b):
        return l*b
    def calculate_perimeter2(self,l,b):
        return 2*(l+b)

shape=shape()
radius=int(input("enter the radius for circle:\n"))
circle=circle(shape)
area=circle.calculate_area()
print(" area of circle is:",area)
perimeter=circle.calculate_perimeter()
print("perimeter of circle is: ", perimeter)
rectangle=rectangle()
area2=rectangle.calculate_area2(10,20)
print("area of rectangle is:",area2)
perimeter2=rectangle.calculate_perimeter2(10,10)
print(" perimeter of rectangle is:",perimeter2)'''
#5)

# Define a class called Node to represent a node in a binary search tree (BST)
'''class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)

# Define a class called BinarySearchTree to represent a binary search tree
class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(4))  # Found, returns the node (4)
print(bst.search(9))'''  # Not found, returns None
#5)Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.
'''class shoppingcart:
    def __init__(self,items,price):
        self.items=items
        self.price=price
    items=input("enter the items")
    for _  in range(0,len(items)):
        rate=int(input("enter the rate"))
    def add(self,items):
        print("enter the items you want to add:")
        return items
    def calculate_total_price(self,price):
        print("the total price is :")
        return self.items*self.rate
shoppingcart=shoppingcart()
add_items=shoppingcart.add(items,price)
calculateprice=shoppingcart.calculate_total_price()
print(add_items)
print(calculateprice)'''
'''class ShoppingCart:
    def __init__(self):
        self.items = {}   
    def add(self, item, price):
        self.items[item] = price
        print(f"Added {item} with price {price} to the cart.")
    def calculate_total_price(self):
        total_price = sum(self.items.values())
        return total_price
shopping_cart = ShoppingCart()
num_items = int(input("Enter the number of items: "))
for _ in range(num_items):
    item = input("Enter the item name: ")
    price = float(input(f"Enter the price for {item}: "))
    shopping_cart.add(item, price)
total_price = shopping_cart.calculate_total_price()
print(f"The total price of items in the cart is: {total_price}")'''
#6)Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.
'''class bank:
    def __init__(self,emp,customer):
        self.emp=emp
        self.customer=customer
    def deposits(self,):'''
'''class BankAccount:
    def __init__(self, account_number, customer_name, initial_balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to account {self.account_number}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: {self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount} from account {self.account_number}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")
        return self.balance


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, customer_name, initial_balance=0):
        if account_number in self.accounts:
            print(f"Account number {account_number} already exists.")
        else:
            new_account = BankAccount(account_number, customer_name, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account created for {customer_name} with account number {account_number}.")

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print(f"Account number {account_number} not found.")
            return None

    def deposit_to_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)

    def withdraw_from_account(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)

    def check_account_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            account.check_balance()


# Example usage:
if __name__ == "__main__":
    my_bank = Bank("MyBank")

    # Create accounts
    my_bank.create_account("123456", "John Doe", 500)
    my_bank.create_account("654321", "Jane Smith", 1000)

    # Deposit money
    my_bank.deposit_to_account("123456", 300)
    my_bank.deposit_to_account("654321", 500)

    # Withdraw money
    my_bank.withdraw_from_account("123456", 200)
    my_bank.withdraw_from_account("654321", 1500)  # This will show an insufficient funds message

    # Check balances
    my_bank.check_account_balance("123456")
    my_bank.check_account_balance("654321")'''




