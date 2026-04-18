"""
Part 3 Filtering
Selecting and filtering data with certain conditions
"""

print("Example 1 Filter numbers > 20")

numbers = [10, 20, 30, 40, 50]

for n in numbers:
    if n > 20:  # this is where condition or filtering, using a if else stetement
        print(n)
"""
The Output like this:

30
40
50

"""

print("\nExample 2 Filter numbers >= 20")


for n in numbers:
    if n >= 20:  # this is where condition or filtering, using a if else stetement
        print(n)

"""
The Output like this:

20         ----> Why 20 on here?
30         Because this stetement '>='  It means a 20 included in the exception conditions
40
50

"""

print("\nExample 3 Real Case Filtering Pattern transactions (positive only)")


transactions = [100, -300, 200, -500, 700, -300, 1000]

for tx in transactions:
    if tx > 0:
        print(f"Valid transaction: {tx} ")

"""
The ouput like this: 

Valid transaction: 100
Valid transaction: 200
Valid transaction: 700
Valid transaction: 1000

"""
