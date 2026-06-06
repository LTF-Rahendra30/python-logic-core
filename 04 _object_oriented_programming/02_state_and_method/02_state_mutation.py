# The case is same at berofe file

class User:
    # Constructor
    def __init__(self,name,balance): # Atributte
        self.name = name 
        self.balance = balance

    # Method
    def get_info(self):
        return f"Welcome: {self.name}"
    
    def deposit(self,amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True
    