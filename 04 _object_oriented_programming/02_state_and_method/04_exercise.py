"""
Scenario: 

Simple sistem Bank Account, every account have:
- owner name
- balance
"""

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balancen = balance

    def deposit(self,amount):
        if amount <= 0:
            return False
        self.balancen += amount
        return True
    
    def withdraw(self,amount):
        if amount > self.balancen or amount <= 0:
            return False
        self.balancen -= amount
        return True
    