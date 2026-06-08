class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True
    
    def withdraw(self,amount):
        if amount > self.balance or amount <= 0:
            return False,None
        self.balance -= amount
        return True
    
user1 = BankAccount("Bob",0)