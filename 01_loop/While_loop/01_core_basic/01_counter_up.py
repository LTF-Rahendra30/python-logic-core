i = 1  # default initialization

while i <= 5:  # condition
    print(i)
    i += 1  # increment or i = i + 1

"""
The output is a:
1
2
3
4
5 

why like this??
  that simple, because the i strart at i = 1, then condition true, then print i, then increment i by 1 , and then the current of is 2, 

  2 is lees than 5, then condition true, then print i again and check the condition again until those condition is false,that is, up to the value of 5, then the loop will stop and the output is 1, 2, 3, 4, 5 
"""

print("\nExample 2, Counter Up number 1 to 10")
# Example 2, Counter Up number 1 to 10

i = 1  # default initialization
while i <= 10:
    print(i)
    i += 1  # increment by 1
"""The output is a:
1
2
3
4
5
6
7
8
9
10
The logic is the same as the previous example, but just different in the condition (i <=10)
"""


print("\nExample 3, Counter up even number from 1 to 10")
# Example 3, Counter up even number from 1 to 10

i = 1  # default initialization

while i <= 10:  # condition
    if i % 2 == 0:
        print(i)
    i += 1  # increment by 1

"""The output is a:
2
4
6
8
10
because the condition cheks if i is even number or not, use the modulus operator (if i % 2 == 0),
if the condition is  true, then print i, and then increment by 1, and then check  the conndition again until the value of i is 10, the even number beetwen 1 to 10 is (2, 4, 6, 8, 10) 

cause previously filtering had been done carried out with the if statement and modulus operator, so the output is 2, 4, 6, 8, 10

"""

print("\nExample 4, Counter up odd number from 1 to 10")
# Example 4, Counter up odd number from 1 to 10

i = 1  # default initialization

while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1  # increment by 1

"""
The output is a:
1
3
5
7
9
because the condition cheks, if i is odd number from 1 to 10 0r not, use the modulus operator (if i % 2 != 0),
if the condition is  true, then print i, and then increment by 1, and then check  the conndition again until the value of i is 10, the odd number beetwen 1 to 10 is (1, 3, 5, 7, 9)

"""
