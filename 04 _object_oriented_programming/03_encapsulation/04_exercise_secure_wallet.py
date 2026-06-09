class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <=0:
            return False
        self._balance +=amount
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

