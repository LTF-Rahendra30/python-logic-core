# agrs = variabel number of positional arguments
# kwargs = variabel number of keyword arguments

# Exampels using agrs
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Usage 
print(sum_all(10,10,10,10,10,20,30))
"""
The ouptut is a 100

cause the numbers of input isn't limited, and how much fixed input will be calculated by addition 

"""


# kwargs

def user_info(**data):
    return data

# Usage 
print(user_info(name="Joel",age="12"))

"""
The output is a dictionary:
{'name': 'Joel', 'age': '12'}

cause args parameters a collection of input that is converted into an dictionary (key:value)

That is flexible for stucture, readable and suitable for data that has label.


"""