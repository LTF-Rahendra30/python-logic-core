data = ["Apple", "Banana", "Cerry"] #Exmple data var
data2 = [1,2,3,4] #Example data 2
data3 = [[1],[2],[3]] # Example nested data 3

# Remove value for index 2 = Banana to Manggo in data 1
for value in range(len(data)):
    data[2] = "Manggo" 
print(data)

# Multiplication 2 to each loop value in data 2
for value in range(len(data2)):
    data2[value] *= 2
print(data2)

# Loop Remove real value in data 3
for value in data3:
    value[0] *= 2
print(data3)

