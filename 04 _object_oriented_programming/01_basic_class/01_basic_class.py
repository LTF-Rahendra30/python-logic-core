# Whitout Class
merk1 = "Ferarri"
merk2 = "lamborgini"

price1 = 400000
price2 = 600000

def setup(merk,price):
    print(f"Car: {merk} Price: {price}")

# Create
print("========== Without OOP ==========")
car1 = setup(merk1,price1)
car2 = setup(merk2,price2)
"""
This is work, but this code isn't scalabele,separate data, and very diffucult to maintain
"""

# With Class
class SuperCar:
    # Artibute of the Car
    def __init__(self,merk,owner,color):
        self.merk = merk
        self.color = color
        self.owner = owner
        self.max_speed = 0
        self.price = 500000 

    # Method
    def setup(self):
        print(f"Car: {self.merk}| Owner: {self.owner} | Color: {self.color}")
    def car_speed(self,add_speed):
        if self.max_speed >= 200:
            return(False, f"This isn't a Super Car! ")
        self.max_speed += add_speed
        return (True, f"Car {self.merk} , now speed: {self.max_speed} km/h")

    def transfer_owner(self,new_owner,city):
        return (True, f"Car: {self.merk} {self.color}, New owner: {new_owner}, city: {city} ")
    
    def buy_my_car(self,your_money,age,new_owner_name,city):
        if your_money < self.price:
            return (False, "You dont have enough money")
        elif your_money > self.price:
                payment = your_money -  self.price
        elif age < 18:
            return(False,"You're not old enough")
        
        valid_buyer = self.transfer_owner(new_owner_name,city)
        return (True,f"Success {valid_buyer}, Your return: {payment}")   


# Create Object

print("========== With OOP ==========")
my_car = SuperCar("McLeren", "Andrew","Grey")
my_car2 = SuperCar("Porche", "Bob","Black")
my_car.setup()
my_car2.setup()
"""
No need to enter input in parameter, because we've entered the input in the parameter when create the objcet

And in the function: 'def __init__' ,we've done the attribute/variabel setup by 'self' 
"""
# speed = my_car.car_speed(250)
# buy = my_car.buy_my_car(520000,19,"bob","Florida")
# print(speed)
# print(buy)