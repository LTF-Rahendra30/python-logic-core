is_login = False

while not is_login:
    ussername = input("Enter username: ")
    password = input("Enter password: ")

    if ussername == "admin" and password == "12345":
        print("Login successful!")
        is_login = True
    else:
        print("Invalid username or password. Please try again.")

"""
Here is a little different from the previous, because:
- We use state based loop, where we have a variable boolean is_login to control the loop, and it will keep asking for username and password until the user enter the correct username and password
- The loop will only stop when the user enter the correct username and password, and it will print the "login successful message", and set the is_login to True, so it will break the loop
- If user enter wrong username or wrong password, it will print "invalid username or password. Please try again." and then loop will continue to repeat the process until the user enter the correct username and password
"""
