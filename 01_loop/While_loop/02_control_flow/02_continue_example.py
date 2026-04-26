i = 0

while i < 5:
    i += 1
    if (
        i == 3
    ):  # The condition is true when i is equal to 3 who is the filter for the continue statement
        continue  # The continue statement when i equal to 3 will skip code and jump to next iteration
    print(i)
print("Loop has ended")

"""
Output:
1
2
4
5
Loop has ended

why like this? that simple:
- The while loop starts with i equal to 0.
- The loop will continue as long as i is less than 5.
- when i reaches 3, the if statement is true, and the continue statement is executed.
- The continue statement will skip and jump to the next iteration of the loop
- So, when i is 3, it will not be printed, and the loop will continue with the next value of i.
- The loop will print 1, 2, 4, and 5, whitout printing 3.
- After the loop finishes, it will print "Loop has ended".
"""
