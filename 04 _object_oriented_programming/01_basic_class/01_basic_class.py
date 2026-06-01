
# The Class of Car
class Car:
    # Artibute of the Car
    def __init__(self,color,fuel,mileage,speed):
        self.color = color
        self.fuel = fuel
        self.mileage = mileage
        self.speed = speed
        self.cost = 0
    
    def calculate_cost_fuel(self,speed,fuel,mileage):
        return self.cost (mileage / speed) * fuel

car1 = Car("red",10,100,50)
print(car1.cost)