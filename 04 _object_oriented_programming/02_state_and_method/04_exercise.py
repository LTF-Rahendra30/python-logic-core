"""
Scenario: 

Simple sistem Bank Account, every account have:
- owner name
- balance
"""

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def get_info(self):
        return f"Name: {self.name} | Balance: {self.balance}"
    
    def deposit(self,amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True, self.get_info()
    
    def withdraw(self,amount):
        if amount > self.balance or amount <= 0:
            return False
        self.balance -= amount
        return True
    
    def transfer(self,target_account,amount):
        if amount > self.balance or amount <= 0:
            return False

user1 = BankAccount("bob",100)
print(user1.deposit(100))