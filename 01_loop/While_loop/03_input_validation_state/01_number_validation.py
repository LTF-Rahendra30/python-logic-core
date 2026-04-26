while True:
    user_input = input("Please enter a number > 10: ")

    if user_input.isdigit():  # Checking if the input is a valid number
        number = int(user_input)

        if number > 10:
            print("Valid number! You entered:", number)
            break
        else:
            print("Invalid number. Please enter a number greater than 10.")
    else:
        print("Invalid input, must be a number.")

"""
The output like this:

1. Please enter a number > 10: abc
Invalid input, must be a number.
    cause "abc" is not a valid number, and not valid in isdigit() function

2. Please enter a number > 10: 5
Invalid number. Please enter a number greater than 10.
    cause "5" is a valid number, but it is not greater than 10

3. Please enter a number > 10: 15
Valid number! You entered: 15
    cause "15" is a valid number, and it is greater than 10, so it will break the loop and print the valid number
"""
