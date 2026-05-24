# recursion

# Recursion is a function that calls itself to solve smaller versions of the same problem. It must have 
# 1. base case
# 2. Reursive case (to continue)

def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a - 1)

print(factorial(5))
# print(factorial(0))   This erors 
# print(factorial(-1))

"""
The output: 120, because:

a = 5, return a = 5 x factorial(4) = 20
a = 4, return 20 x 3 = 60
a = 3, return 60 x 2 = 120
a = 2, return 120 x 1 = 120

the result of factorial 5 is a 120

"""
