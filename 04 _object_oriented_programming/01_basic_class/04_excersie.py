class User():
    def __init__(self,name,age,balance):
        self.name = name
        self.age = age
        self.balance = balance

    def introduce_user(self):
        print(f"Hello {self.name}")
    
    def can_afford(self,price):
        if price <= self.balance:
            return(False,"You cant buy something by your balance")
        self.balance -= price
        return (True,f"Success, your balance now at {self.balance}")