class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return True
    
    def withdraw(self,amount):
        if amount > self.balance or amount <= 0:
            return False,None
        self.balance -= amount
        return True

# Create Object
user1 = BankAccount("bob",100)
user2 = BankAccount("jerry",350)

print("before: ",user1.balance)

# Normal Usage
user1.withdraw(50)
print("After withdraw: ",user1.balance)

"""
The output:

before:  100
After withdraw:  50

This is like a normal
"""

# Breaak The System
user1.balance = -99999999
print("Hacked balance:", user1.balance)
"""
The output:

before:  100
After withdraw:  50
Hacked balance: -99999999  # The State could manipulation, and whitout validation, and also the method useless


"""