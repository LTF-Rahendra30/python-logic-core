"""
Part 4
Max / Min without built-in function
"""

print("Example 1, Find Max")

numbers = [5, 10, 15, 1, 8]

max_value = numbers[0]

for n in numbers:
    if n > max_value:
        max_value = n
print(f"Max Value: {max_value}")

"""
The output is a:
15

but why like this??

because :
start at 5
If 5 greater than 10??? ----> Yes 
If 10 greater than 15 ----> Yess
If 15 greater than 1 -----> Noo
If 15 greater than 8 -----> Noo

The conclusion is a: 15 is a Max value in the list 'numbers = [5, 10, 15, 1, 8]'
Thats simple

"""

print("\nExample 2, Find Min")

numbers = [9, 11, 8, 3, 14]

min_value = numbers[0]

for n in numbers:
    if n < min_value:
        min_value = n
print(f"Min Value: {min_value}")

"""
The output is a:
3

because 
start at 9
If 11 less than 9 ----> Noo, then 9 will be a the min_value
If 9 less than 8?? ---> Noo, then 8 will be a the min_value
If 8 less than 3?? ---> Noo, then 3 will be a the min_value
If 3 less than 14?? ---> Noo, then 3 will be a the min_value

The conclusion is a: 3 is a Min value in the list 'numbers = [9, 11, 8, 3, 14]'
Thats Simple 

"""

print("\nReal Case to Find largest Whale transactions crypto")

transactions = [1800, 12000, 4800, 3500, 5900, 34000, 10000, 6700, 7400]

max_trx = transactions[0]

for trx in transactions:
    if trx > max_trx:
        max_trx = trx

print(f"The Lergest Transactions is: {max_trx}")
