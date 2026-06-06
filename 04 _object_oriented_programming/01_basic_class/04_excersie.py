""""
The simple scenario:

There are 3 user:

- name
- age
- balance

And there is a function:

- introduce user()
- can_afford() chek if the user can buy something (sufficient balance or not)
"""

class User():
    def __init__(self,name,age,balance):
    
        
        # Error handling
        if balance and age <= 0:
            raise ValueError("Cant be zero or Negative")
        self.name = str(name)
        self.age = int(age)
        self.balance = int(balance)
        

    def introduce_user(self):
        return f"Hello {self.name} | age: {self.age} | Balance: {self.balance}"
    
    def can_afford(self,price):
        if price > self.balance:
            return(False,"You cant buy something by your balance")
        return(True,"Your Eligible")
    def spend(self,amount):
        if amount > self.balance:
            return (False, "Your balance isnt enough")
        self.balance -= amount
        return (True,f"Success buy, your balance now at {self.balance}")
# Create Object
try:
    user1 = User("Bob",1,10000)
    print(user1.introduce_user())
    print(user1.can_afford(1000))
    print(user1.spend(2000))
except ValueError as e:
    print(f"Errors for create objcet: {e}")