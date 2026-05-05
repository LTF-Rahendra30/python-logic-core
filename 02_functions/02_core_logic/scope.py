"""
The global variabels & Local variabels
"""

# Changing global variabels inside function but This is eror, because global variabels can't be changed
"""
total = 0
def num():
    total = total + x


num(5)
"""

# GLOBAL Variabels can be read in the function
x = 10


def get():
    print(x)


get()
"""
The output is value of the x variabels : 10
"""

"""
def num():
    y = 10


num() # This output is a: 10
print(y) # is undefined, because y is local variabels in the loop

"""

# variabels names are the seme between GLOBAL Var and LOCAL, then this:
age = 17  # Global Var


def young():
    age = 18  # Local Var
    print(age)  # Print Var


young()
"""
The ouput is a : 18, because Global var are overwritten by local var
"""
