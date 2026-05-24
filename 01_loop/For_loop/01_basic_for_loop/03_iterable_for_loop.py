#Velue & Referance
#Mutable Loop & Imuntable Loop

# Example data var
data = [10,20,30]
data2 = [[10],[20],[30]]

# Imuntable Loop by memory and data var
for i in data:
    i *= 2
    print(i) #Changed in Loop
print(data) # Not Changed After Loop and outside the Loop

print("================================")

# Mutable Loop by memory and data var
for i in range(len(data)):
    data[i] *= 2
    print(data[i])
print(data)

print("================================")

# Mutable loop by memory and nested list data

for i in data2:
    i[0] *= 2 # Changed individual value in nested list data, to multiplication 2
print(data2)