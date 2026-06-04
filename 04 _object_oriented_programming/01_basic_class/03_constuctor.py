
# Without Constuctor
class Student():
    gpa = 0
    name = ""

    def setup(self,gpa,name):
        self.name = name
        self.gpa = gpa

# Create Object without consturctor
student = Student()
student.setup(400,"Bob")
print(student.name)
print(student.gpa)
"""
This is manual call object, because whitout constructor deffinition at the beginning
"""


print("=" * 50)

# With Constructor
class Student2():
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
student = Student2("Andrew",300)
print(student.name)
print(student.gpa)
"""
Create object with constructor, without having to do it manually
"""
