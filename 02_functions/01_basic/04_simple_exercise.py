# Simple Excercise: Result after discount

"""
- The User buys goods
- The Shop gives a discount

"""


# Calculate discount amount
def calculate_discount_amount(price, discount):
    return (discount / 100) * price


# Calculate total price
def final_price(price, discount):
    discount_amount = calculate_discount_amount(price, discount)
    return price - discount_amount


# Run input and output logic
def main():
    try:
        price = float(input("Enter your price: "))
        discount = float(input("Enter your discount: "))

        if discount < 0 or discount > 100:
            print("Invalid discount")
        else:
            total = final_price(price, discount)
            print(f"Total Price {total}")

    except ValueError:
        print("Eror, must be a number ")


if __name__ == "__main__":
    main()
