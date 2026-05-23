# Error handling with function

# Function should handle invalid input sefely
# Two approaches
# 1, validation (check condition)
# 2. Exception handling (try-except)


# Without validation and handling
def divide(a,b):
    return a / b

# print(divide(10,0))
"""
The  output can't checking the input value, that zero or positive number or other, maybe input can string not integer
"""

# With handling
def safe_divide(a,b):
    if b == 0:
        return "Errors: division by zero"
    return a / b
print(safe_divide(100,10))
"""
The output is 10, and then the function is safe cause using validation (if) in the function
"""

# Try Except
def safe_divide_with_exception(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Errors: division by zero"
    except TypeError:
        return "Errors: invalid type"
    

# Usage
print(safe_divide_with_exception(10, 2))
print(safe_divide_with_exception(10, 0))
print(safe_divide_with_exception(10, "a"))

"""
The outout:
5
Errors: division by zero
Errors: invalid type


Insight:
- Validation prevents predictable erors
- Exception handling catches unexpected errors
- Good function should be predictable and safe
"""