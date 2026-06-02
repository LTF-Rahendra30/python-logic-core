
# The Class of Car
class SuperCar:
    # Artibute of the Car
    def __init__(self,merk,color):
        self.merk = merk
        self.color = color
        self.max_speed = 0

    # Method
    def car_speed(self,add_speed):
        if add_speed <= 200:
            return(False, f"This isn't a Super Car! ")
        self.max_speed += add_speed
        return (True, f"Car {self.merk} , now speed: {self.max_speed} km/h")

    def transfer_owner(self,new_owner,city):
        return (True, f"Car: {self.merk} {self.color}, New owner: {new_owner}, city: {city} ")
        
# Create Object

my_car = SuperCar("McLeren", "Grey")
my_car.car_speed(200)
my_car.transfer_owner("Bob","Sydney")