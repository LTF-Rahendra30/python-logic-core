class University:
    # Add atribute
    def __init__(self,location,acreditation,world_rank):
        self.location = location
        self.acreditation = acreditation
        self.world_rank = world_rank

class Student:
    pass

# Create Object
university1 = University("NYC","A","20")
print(type(university1)) # Type : CLass