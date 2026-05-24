#Hi everyone, as promised yesterday, I'll discuss why the loop results start from 0??


data = ["apple", "banana", "mango"]

for index, fruit in enumerate(data, start=1):
    print(index, fruit)
  
#Use "start= n" to create an index from anywhere, from 1,from 2, you can change the index as you like

print("\n----------------\n")

#Example multiplication velue list with enumerate

char = ["A","B","C","D"]

for i, value in enumerate(char):
    print(i +1, value *2 )


print("\n----------------\n")

#Example for crypto transaction hash

transaction_hash = [
    "0xabcd900",
    "0x32abbs0",
    "0x23bcx22",
    "0x19zfab9"
]

for i, trx in enumerate(transaction_hash,start=1):
    print("Index: ",i,"Transaction hash: ",trx)