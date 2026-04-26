while True:
    print("1. Say Hello")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
        break  # Exit the loop and end the program
    else:
        print("Invalid choice. Please try again.")

"""
The ouput of this code will be:
1. Say Hello
    when the user enters 1, it will print "Hello!" and show the menu again.
    why? because the loop is infinite and will continue until the user chooses to exit by entering 2.

2. Exit
    when the user enters 2, it will print "Goodbye!" and break the loop, ending the program.
    why? because the break ststement in the elif block code will exit the loop when the user chooses to exit, And the program will end.

3.Invalid choice. Please try again.
    when the user enters any other input that is not 1 or 2 (like any number or text), it will print "Invalid choice. Please try again." and show the start menu again.
"""
