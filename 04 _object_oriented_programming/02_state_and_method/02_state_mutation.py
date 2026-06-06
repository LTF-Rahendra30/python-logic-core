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

user1 = User("Bob",100)
print(user1.get_info()) # Before Deposit the balance is zero
print(user1.deposit(100))
print(user1.get_info()) # After Deposit and Before Withdraw the balance is 1000
print(user1.withdraw(10))
print(user1.get_info()) # After Withdraw the balance is 800