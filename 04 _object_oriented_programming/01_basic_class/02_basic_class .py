class University:
    # Add atribute
    def __init__(self,location,acreditation,world_rank):
        self.location = location
        self.acreditation = acreditation
        self.world_rank = world_rank

# Without __init__ to encapculation atribute and method in the class
class Student:
    name = ""
    gpa = 0

    def introduction(self):
        print(f"Helo, my name: {self.name}")
    def say_hello(self,name):
        print(f"Hello! {self.name} my name is {name}, the person who said hello to you")
# Create Object
university1 = University("NYC","A","20")
print(type(university1))# Type : CLass
print(university1.location) # NYC
print(university1.acreditation) # A
print(university1.world_rank) # 20

# Create manual atribut and method without definded atribute by __init__
print("="* 100)
student1 = Student()
student1.name = "Bob"
student1.introduction() # Helo, my name: Bob
student1.say_hello("Choki") # Hello! Bob my name is Choki, that someone who say hello to you