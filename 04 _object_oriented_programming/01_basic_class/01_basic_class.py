
# The Class of Car
class Car:
    # Artibute of the Car
    def __init__(self,merk,color):
        self.merk = merk
        self.color = color
        self.max_speed = 0

    # Method
    def car_info(self,add_speed):
        self.max_speed += add_speed
        return (True, f"Car {self.merk} , now speed: {self.max_speed} km/h")

    def transfer_owner(self,new_owner,city):
        return (True, f"Car: {self.merk} {self.color}, New owner: {new_owner}, city: {city} ")
        
