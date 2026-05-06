"""
Compotition Function

This file paractice case study about Simpel system chekout.
The users can buy good and calculation this:
- Discount
- Tax
- Shipping cost (besed on weight)

"""


# Function for calculate discount
def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)


# Function for calculation tax
def applly_tax(price, tax_percent):
    return price + (price * tax_percent / 100)


# Function for calculation shipping cost (in Kilogram/Kg)
def calculation_shipping(weight):
    return weight * 1000  # The shipping cost default calculation (1000 cost /kg)


# Function for calculation the total final users payment: after discount,after tax,after shipping cost
def chekout(price, discount_percent, tax_percent, weight):
    after_discount = apply_discount(price, discount_percent)
    after_tax = applly_tax(after_discount, tax_percent)
    shipping_cost = calculation_shipping(weight)
    return after_tax + shipping_cost


def main():
    try:
        price = float(input("Enter your price: "))
        discount_percent = float(input("Enter your discount: "))
        tax_percent = float(input("Enter your tax: "))
        weight = float(input("Enter weight of your item: "))

        if price <= 0:
            print("The price must be greater than 0")
        elif discount_percent > 100 or discount_percent < 0:
            print("The Discount Percent must be greater than 0 and <100")
        elif tax_percent > 100 or tax_percent < 0:
            print("The Tax Percent must be greater than 0 and <100")

        else:
            final_price = chekout(price, discount_percent, tax_percent, weight)
            print(f"Your total payment: {final_price}")

    except ValueError:
        print("Eror, must be a number ")


if __name__ == "__main__":
    main()
