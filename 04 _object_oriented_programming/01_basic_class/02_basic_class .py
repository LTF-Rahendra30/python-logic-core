class University:
    # Add atribute
    def __init__(self,location,acreditation,world_rank):
        self.location = location
        self.acreditation = acreditation
        self.world_rank = world_rank

# Without __init__
class Student:
    name = ""
    gpa = 0

    def introduction(self):
        print(f"Helo, my name: {self.name}")
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
student1.introduction()