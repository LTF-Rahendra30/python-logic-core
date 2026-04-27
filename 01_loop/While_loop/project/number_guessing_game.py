"""The number guessing game (1-10)
The user is asked to guess the  number between 1-10, The rules like this:
- Users are given the opportunity to guess 5 times
- Every wrong guess (samller or bigger) the chance chance to guess is reducing by 1
- If the users enters a negative number,decimal number, enters a lettef/alfabet and string, the chance is still reduced
"""

import random

secret_number = random.randint(1, 10)
attempts = 5

while attempts > 0:
    try:
        user_input = int(input("\nEnter secret number in range 1-10: "))

        if user_input < 1 or user_input > 10:
            print("Invalid Number! Must be between (1-10)")
        elif user_input > secret_number:
            print("Too High")
        elif user_input < secret_number:
            print("Too low")
        else:
            print(f"Your guess is valid! {secret_number}")
            break
    except ValueError:
        print("Please don't enter decimmal or string")

    attempts -= 1
    print(f"Your have {attempts} chances left to guess")

if attempts == 0:
    print("Your Lose")
    print(f"Correct!, The secret number is {secret_number} ")
