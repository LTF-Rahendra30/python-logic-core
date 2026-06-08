class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self._balance += amount
        return True

    def withdraw(self, amount):
        if amount > self._balance or amount <= 0:
            return False
        self._balance -= amount
        return True
    
acc = BankAccount("Bob", 100)

print("Balance:", acc.get_balance())

acc.deposit(50)
print("After deposit:", acc.get_balance())

acc.withdraw(30)
print("After withdraw:", acc.get_balance())

# Actually, we can manipulation this state, but should be dont do it, all changes only through the method
# acc._balance = 99999