# Copyright 2026 LTF30
# Hello everyone,today I learned about loop enumeration, I hope this repository will be useful for you and me in the future.


#Example list for today.This list has 3 index and 3 values 
data = ["apple","banana","mango"]

for index, value in enumerate(data):
    print(index, value)
    
#The output from of the list above is:
#(index,value)
#index starts from 0 to 2
#value starts from "apple to mango"
#This looo has 2 variabel, namely: index and value

#Example transaction data in blokchain with enumerate 

transactions = [
"0xa1f4",
"0xb9c2",
"0xf331"
]

for index, tx in enumerate(transaction):
    print("Transaction", index, ":", tx)
