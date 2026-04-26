correct_password = "12345"
attempts = 0

while attempts < 3:
    password = input("Please enter the password: ")

    if password == correct_password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Please try again.")
        attempts += 1

if attempts == 3:
    print("Your account is locked.")

"""
The output like this:

1. Please enter the password: abc
Incorrect password. Please try again.
    cuase "abc" is not the correct password, so it will print the incorrect password message and increment the attempts by 1

2. Please enter the password: 1234
Incorrect password. Please try again.
    cause "1234" is not the correct password, it's same as then prevoius case

3. When you enter wrong password or wrong text until 3 times, The program will print "Your account is locked." because the attempts is equal to 3, and it will not allow you to try again
4. Please enter the password: 12345
Access granted!
    cause "12345" is the correct password, so it will print the access granted message and break the loop, and it will not check the attempts anymore
"""
