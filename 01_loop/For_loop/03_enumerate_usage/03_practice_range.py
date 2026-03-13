# Copyright 2026 LTF30
#03_practice_range
#Practice:  Using range() with lists

# Example 1 - Basic range loop
print("Example 1: Basic range")

for i in range(1,5):
    print(i)

print("\n---------------------\n")

# Example 2 - Using range with list index
print("Example 2: Acces list elements")

numbers = [10,20,30,40]

for i in range(len(numbers)):
    print("Index: ",i, "Velue: ", numbers[i])

print("\n---------------------\n")

#Example 3 - Modify list using range
print("Example 3: Modify list value")

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print("Updated list: ",numbers) #Index velue is multiplied by the integer 2

print("\n---------------------\n")

#Example 4: Accumulation pattern
print("Example 4: Cumulative addition")

numbers = [1,2,3,4]

#Loop start from index 0
for i in range(len(numbers)):
    numbers[i] += numbers[i-1] # Addition value index with previous index velue
print("Result: ", numbers)

print("\n---------------------\n")

numbers = [1,2,3,4]
#Loop start from index 1 
for i in range(1,len(numbers)):
    numbers[i] += numbers[i-1] # Addition value index with previous index velue
print("Result: ", numbers)

print("\n---------------------\n")

numbers = [1,2,3,4]
#Loop reverse iteration
for i in range(len(numbers)-1,-1,-1):
    numbers[i] += numbers[i-1]
print("Result after reverse: ",numbers)

print("\n---------------------\n")

#Example 5 - using sum()
print("Example 5: Sum of list")

numbers = [10,20,30,40,50]
print("Sum:", sum(numbers))

print("\n---------------------\n")

#Example 6 Accumulation pattern using sum()
print("Example 6: Addition index value and sum all index velue after loop")

for i in range(len(numbers)):
    numbers[i] += numbers[i-1]
print("Result after add & sum: ", sum(numbers))





