class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self._balance = balance # Protacted

    def deposit(self,amount):
        if amount <= 0:
            return False
        self._balance += amount
        return True
    
    def withdraw(self,amount):
        if amount > self._balance or amount <= 0:
            return False,None
        self._balance -= amount
        return True
    
acc = BankAccount("Bob", 100)

print("Before:", acc._balance)

# 🔥 CAN be DIHACKED
acc._balance = -1000
print("Hacked:", acc._balance)

"""
Output: 

Before: 100
Hacked: -1000

The state in this objcet can still be manipulation
"""