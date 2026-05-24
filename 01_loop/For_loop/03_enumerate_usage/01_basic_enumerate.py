# Copyright 2026 LTF30
# Hello everyone,today I learned about loop enumeration, I hope this repository will be useful for you and me in the future.


#Example list for today.This list has 3 index and 3 values 
data = ["apple","banana","mango"]

for index, value in enumerate(data):
    print(index, value)
    
#The ouotput is like this

""" 
0 apple
1 banana
2 mango
"""
    
#The output from of the list above is:
#(index,value)
#index starts from 0 to 2
#value starts from "apple to mango"
#This looo has 2 variabel, namely: index and value

print("/n----------------/n")

#Another example name data with enumerate

data = [
    "Adams"
    "Bobby"
    "Charley"
    "Dory"
]

for index, name in enumerate(data):
    print(index, name)

#The output is like this 

"""
0 Adams
1 Bobby 
2 Charley 
3 Dory
"""
print("/n----------------/n")

#Example transaction data in blokchain with enumerate 
transactions = [
"0xa1f4",
"0xb9c2",
"0xf331"
]

for index, tx in enumerate(transactions):
    print("Transaction", index, ":", tx)


#The Output is like this:

"""
Transaction 0 : 0xa1f4
Transaction 1 : 0xb9c2
Transaction 2 : 0xf331

"""
# but why does the output start from index 0 ?? 
# I will explain in the next file
