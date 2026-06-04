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
        self.name = name
        self.age = age
        self.balance = balance
        self.price = 0

    def introduce_user(self):
        print(f"Hello {self.name} | age: {self.age} | Balance: {self.balance}")
    
    def can_afford(self,price):
        if self.price >= self.balance:
            return(False,"You cant buy something by your balance")
        self.balance -= price
        return (True,f"Success, your balance now at {self.balance}")

# Create Object   
user1 = User("Bob",12,10000)
user1.introduce_user()
print(user1.can_afford(1000))