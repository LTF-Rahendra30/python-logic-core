"""
Part 2 Counter
Using loops to count events or the number of
components that meet certain conditions
"""

# Example 1


number = [1, 2, 3, 4, 5]

count = 0

for n in number:
    count += 1
print("count: ", count)
"""
The output like this:
5

    But, Why the output is a 5??

Oke,right, that simple....
The output is a 5 because, the vairables 'number' have a 5 conditions that are met to count events

"""

# Example Again

number = [10, 20, 30, 40, 50]

count = 0

for n in number:
    if n > 20:
        count += 1
print("count: ", count)

"""
The output like this:
3

seems to be the same as before, but added the conditions
with if statement

"""
# Example real case, balance transaction on desentralized wallet

transaction = [100, 300, -200, 400, -100]

balance = 0

for tx in transaction:
    if tx > 0:
        balance += 1
print("Balance: ", balance)
