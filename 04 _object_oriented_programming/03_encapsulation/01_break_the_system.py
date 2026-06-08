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