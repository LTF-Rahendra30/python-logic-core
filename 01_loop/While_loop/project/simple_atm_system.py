"""
A simple ATM Machine system, the users can get:
- Check Balance
- Deposit
- Withdraw
- Exit

The rules:
- In the menu, users can't be enter: numbers other than 1-4 and (zero or negative) and can't be enter string or alfabet
- In the deposit option, users can't be enter: numbers other than 1-4 and (zero or negative) and can't be enter string or alfabet
- In the withdraw option, users can't be enter: numbers other than 1-4 and (zero or negative) and can't be enter string or alfabet

All rules are controled and handled by try-except and if-elif-else stetement
"""

print("1.Check Balance\n2. Deposit\n3. Withdraw\n4.Exit ")
balance = 0

while True:
    try:
        user_choice = int(input("\nEnter your choice: "))

        if user_choice == 1:
            print(f"Your Balance: {balance}")

        elif user_choice == 2:

            try:
                input_deposit = int(input("Enter Your deposit: "))

                if input_deposit <= 0:
                    print("Just positive number and not zero! ")

                elif input_deposit > 0:
                    balance += input_deposit
                    print(f"Your Deposit {input_deposit} is Succesed! ")
                    print(f"Your balance: {balance}")
            except ValueError:
                print("Must be number, not string or alfabet! ")

        elif user_choice == 3:
            try:
                input_withdraw = int(input("Enter your withdraw: "))

                if input_withdraw <= 0:
                    print("Withdraw Invalid, because can't be negative or Zero!")

                elif input_withdraw > balance:
                    print("Your balance is low")

                else:
                    balance -= input_withdraw
                    print("Your withdraw is Succesed")
                    print(f"Your balance now: {balance}")
            except ValueError:
                print("Must be number, not string or alfabet! ")

        elif user_choice == 4:
            print("Exit menu")
            break

        else:
            print("Plase enter the avaliable menu!")

    except ValueError:
        print("Plase enter the avaliable menu!, not string or alfabet")
