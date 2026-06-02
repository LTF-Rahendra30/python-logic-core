
# The Class of Car
class SuperCar:
    # Artibute of the Car
    def __init__(self,merk,color):
        self.merk = merk
        self.color = color
        self.max_speed = 0
        self.price = 500000 

    # Method
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

my_car = SuperCar("McLeren", "Grey")
speed = my_car.car_speed(250)
buy = my_car.buy_my_car(520000,19,"bob","Florida")
print(speed)
print(buy)