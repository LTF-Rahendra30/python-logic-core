# The case is same at berofe file

class User:
    # Constructor
    def __init__(self,name,balance): # Atributte
        self.name = name 
        self.balance = balance

    # Method
    def get_info(self):
        return f"Welcome: {self.name} | balance: {self.balance}"
    
    def deposit(self,amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True
    
    def withdraw(self,amount):
        if amount <= 0 or amount > self.balance:
            return False
        self.balance -= amount
        return True
user1 = User("Bob",0)
user2 = User("Andrew",0)
"""
These are two different objcet, and have their own state i the memory
"""

user1.deposit(100)
user2.deposit(50)

print(user1.get_info())
print(user2.get_info())