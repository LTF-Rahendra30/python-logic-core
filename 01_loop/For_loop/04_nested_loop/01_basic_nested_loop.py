# Copyright 2026 LTF30
# Hello everyone,today I learned about nested loop, I hope this repository will be useful for you and me in the future.

"""
Module 4
Basic Nested Loop

Uderstanding how a loop works inside another looop
"""

# Example basic nested loop 1
print("Example 1: Basic nested loop")
for i in range(1,3):
    for j in range(1,4):
        print(i,j)



#The ouput like this
"""
1 1
1 2
1 3
2 1
2 2
2 3
"""

""" But why the ouyput like this??:
    So, outer loop (for i in range(1,3)) = loop 2 times, because range starts from 1 and ends at 2
    and inner loop (for j in range(1,4)) = loop 3 times, because range starts from 1 and ends at 3 
"""

print("\n----------------\n")

#Example nested loop 2 if each velue is printed
print("Example 2: Outher vs Inner loop")

for outher in range(1,3):
    print("Outher loop: ",outher)

    for inner in range(1,4):
        print(" Inner loop: ",inner)
