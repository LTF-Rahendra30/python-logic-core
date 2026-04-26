i = 1

while True:  # this infinitie loop will continue until we break it
    print(i)
    if i == 5:  # When i is equal to 5, the loop will stop executing
        break  # the break statement will exit the loop immediately
    i += 1
print("Loop has ended")  # This line will be executed after the loop is broken

"""
Output:
1
2
3
4
5
Loop has ended

why like this? that simple:
- The while loop starts with i equal to 1.
- The loop will continue indefinitely because the condition is True.
- When i reaches 5, the if statement is true, and the break statement exits the loop.
- break is exiting the loop immediately, so the next line after the loop is executed, which prints "Loop has ended".
- whitout the break stetement, the loop is infinitie and will never end
- Using break, we can control when loops stop executing
"""
