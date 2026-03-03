#Today I'm start study basic Range iteration loop for Python

#Exampele data var
data = [100,200,300]

#Start loop index data to 1 
for i in range(1, len(data)):
    data[i] += data[i-1]
print(data)

print("=======================")

data = [100,200,300]

for i in range(len(data)):
    data[i] += data[i-1]
print(data)

print("=======================")

data = [100,200,300]

for i in range(len(data)-1,-1,-1):
    data[i] += data[i-1]
print(data)