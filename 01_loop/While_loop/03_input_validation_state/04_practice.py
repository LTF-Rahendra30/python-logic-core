# The Validation number greater than 0  , handle eror using try-except statement, and use break statement to exit the loop when the user enter a valid number

attempts = 0

while attempts < 3:
    try:
        user_input = int(input("Enter number greater than 0: "))

        if user_input > 0:
            print(f"Your number is valid! {user_input}")
            break
        else:
            print("Must be > 0")
    except ValueError:
        print("Invalid Input! Just a number! or Not Decimal Number!")

    attempts += 1
    print(f"Your failed : {attempts} times")
if attempts == 3:
    print("Your Failed")
