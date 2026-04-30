"""
A simple command-line wallet system that simulates basic web3 wallet behavior
The users have a default wallet address and default wallet balance by included

wallet addres : 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
balance : 1000

"""

print("A simple crypto wallet simulation")
print("1.Check Wallet Info\n2.Receive Funds\n3.Send Transaction\n4.Exit")

wallet_addres = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"
balance = 1000

while True:
    try:
        user_choice = int(input("\nEnter your choice: "))

        if user_choice == 1:
            print(f"Your Wallet Addres: {wallet_addres}")
            print(f"Your Balance: {balance}")

        elif user_choice == 2:
            try:
                receive_balance = int(input("Enter amount: "))

                if receive_balance <= 0:
                    print("Receive Invalid, because can't be negative or Zero!")
                else:
                    balance += receive_balance
                    print(f"Your addres: {wallet_addres}")
                    print(f"Your receive: {receive_balance}")
                    print(f"Your balance now {balance}")
                    print("Your receive is succeded")

            except ValueError:
                print("Must be number, not string or alfabet")

        elif user_choice == 3:
            while True:
                print(f"Your Wallet Balance: {balance}")
                destination_addres = input("Enter Addres to Send: ")
                if destination_addres == "":
                    print("Cannot be emptied!")
                else:
                    break

            try:
                amount = int(input("Enter Amount: "))

                if amount <= 0:
                    print("Send Invalid, because can't be negative or Zero!")
                elif amount > balance:
                    print("Your balance is low")
                else:
                    print("\nConfim this Transaction")
                    print(f"From Addres: {wallet_addres}")
                    print(f"To Addres: {destination_addres}")
                    print(f"Value: {amount}")
                    confim_trx = input("Confim transaction? (y/n): ")

                    if confim_trx == "n":
                        continue
                    elif confim_trx == "y":
                        balance -= amount
                        print("\nConfimed Transaction")
                        print(f"From Addres: {wallet_addres}")
                        print(f"Send to Addres: {destination_addres}")
                        print(f"Value: {amount}")
                        print(f"Your Balance {balance}")
                        print(f"Transaction Succeeded! ")

                    else:
                        print("Please enter the avaliable menu!")

            except ValueError:
                print("Must be number, not string or alfabet")

        elif user_choice == 4:
            print("Exit menu")
            break

        else:
            print("Plase enter the avaliable menu!")

    except ValueError:
        print("Plase enter the avaliable menu!, not string or alfabet")
