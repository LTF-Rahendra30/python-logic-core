# The Break statement, printing numbers from 1 to 10, but it will stop when it reaches 7

print("Break Statement Example:")

i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1

# The Continue statement, printing numbers from 1 to 10, but it will skip the number 5

print("\nContinue Statement Example:")
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

# The menu system
print("\nMenu System Example:")

while True:
    print("\nMenu:")
    print("1. Hello")
    print("2. Summation Numbers")
    print("3. Exit")

    user_input = input("Please enter your choice (1, 2, or 3): ")

    if user_input == "1":
        print("Hello!")
    elif user_input == "2":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    elif user_input == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
