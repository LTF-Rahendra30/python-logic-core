class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0 or self._balance + amount > 1000:
            return False
        self._balance += amount
        return True

    def withdraw(self, amount):
        if amount > self._balance or amount <= 0:
            return False
        self._balance -= amount
        return True
    
    def transfer(self, target_wallet, amount):
        # Call method
        success = self.withdraw(amount)

        if not success:
            return False
        target_wallet.deposit(amount)
        return True

# Test
w1 = Wallet("Alice",100)
w2 = Wallet("Bob",50)

# get info
print("Before:")
print(f"wallet 1: {w1.get_balance()}, Wallet 2: {w2.get_balance()}")

"""
The output:
Before:
wallet 1: 100, Wallet 2: 50 
"""

# Deposit
print(f"Deposit wallet 1: {w1.deposit(900)}, now balance at: {w1.get_balance()}")

# Todo test transfer 
w1.transfer(w2,30)
"""
The output:
Deposit wallet 1: True, now balance at: 1000

if balance + amount deposit > 1000, deposit is fail
"""


# Get info
print("After:")
print(f"wallet 1: {w1.get_balance()}, Wallet 2: {w2.get_balance()}")
"""
The output:

After:
wallet 1: 970, Wallet 2: 80

"""