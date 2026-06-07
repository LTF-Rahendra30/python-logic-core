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
        return True, "Deposit:",self.get_info()
    
    def withdraw(self,amount):
        if amount > self.balance or amount <= 0:
            return False,None
        self.balance -= amount
        return True,"Withdraw:", self.get_info()
    
    def transfer(self,target_account,amount):
        # Call method
        success,*_= self.withdraw(amount)

        if not success:
            return False
        
        target_account.deposit(amount)
        return True, f"Transer Succesed, Amount: {amount}", self.get_info()

# Create Object
user1 = BankAccount("bob",100)
user2 = BankAccount("jerry",350)

# User 1
print(user1.get_info())
print(user2.get_info())
print(user1.deposit(50)) # Deposit
print(user1.transfer(user2,50)) # Transfer

# User 2
print(user2.get_info())
