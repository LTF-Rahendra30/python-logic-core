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
        # TODO:
        # 1. withdraw dari self
        # 2. kalau gagal → stop
        # 3. deposit ke target
        pass

