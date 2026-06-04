
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

