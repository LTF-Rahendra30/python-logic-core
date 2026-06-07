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
        return True, self.get_info()
    
    def transfer(self,target_account,amount):
        # Call method
        self.withdraw(amount)
        target_account.deposit(amount)

        return True, f"Transer Succesed to: {target_account}", self.get_info()

# Create Object
user1 = BankAccount("bob",100)
print(user1.get_info())
print(user1.deposit(50))

user2 = BankAccount("jerry",100)
print(user2.get_info())

# Transfer Method
print(user1.transfer(user2,10))
