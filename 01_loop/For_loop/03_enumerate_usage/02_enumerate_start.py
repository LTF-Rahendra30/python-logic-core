#Hi everyone, as promised yesterday, I'll discuss why the loop results start from 0??


data = ["apple", "banana", "mango"]

for index, fruit in enumerate(data, start=1):
    print(index, fruit)
  
#Use "start= n" to create an index from anywhere, from 1,from 2, you can change the index as you like
