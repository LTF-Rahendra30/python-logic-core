class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance # Protacted

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