# Matrix / Grid Example

print("\n3x3 Grid")

for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()


print("\nMultiplication Table(1-3)")

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

print("\nInner loop with i variables")
for i in range(4):
    for j in range(i):
        print(i, j)

"""
Ouput like this:
range(4) ---> (0,1,2,3)

1 0  -> Why like this? because range 0 on range(0) doesn't output
2 0
2 1
3 0
3 1
3 2

"""

print("\nTriangle Pattern Loop")
for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print()
