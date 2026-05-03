# Retun & Print

# Use Return


def using_return(a, b):
    return a + b


# Use Print
def using_print(a, b):
    print(a + b)


# Using
print("Return:")
print(using_return(10, 20))

print("\nUsing Print:")
using_print(10, 20)

"""
The output is the same, is a 30, but there is different:
1. If using return, you can this:
    - provude result
    - can be used in other logic

2. If using print, you can this:
    - only provide result,but if you want add other operations outside the function, it's not possible

    Example:

    def sum_num(a,b):
        print(a + b)
    result = sum_num(10,20) * 2

    This is eror and is doesn't work

"""
