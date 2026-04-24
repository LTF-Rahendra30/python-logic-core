i = 5  # default initialization

while i >= 1:  # condition
    print(i)
    i -= 1  # decrement or i = i - 1

"""
The output is a:
5
4
3
2
1
why like this??
  that simple, because this is the opposite of counter up in the previous file,
  
  i strart at i = 5, then coindition true, then print i, is a 5, then 5 is >= 1,
  then decrement i by 1 (5 - 1 = 4), and then the current of i is 4, and then check conditions  again until those condition is false, 
  
  until the value of i is 1 (i = 1, 1 >= 1 is true, but 0 >= 1 is false), then the loop will stop and the output is 5, 4, 3, 2, 1
  
  """

print("\nExample 2, Counter down number 10 to 1")
# Example 2, Counter down number 10 to 1

i = 10  # default initialization

while i >= 1:  # condition
    print(i)
    i -= 1  # decrement by 1

"""The output is a:
10
9
8
7
6
5
4
3
2
1

because the logic is the same as the previous example, but just different in the condition (i >= 1)
"""
