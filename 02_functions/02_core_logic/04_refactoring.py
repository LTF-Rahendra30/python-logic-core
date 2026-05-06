"""
Refactoring : Change the code structure to be cleaner using functions
"""

# A Code structure without function
print("Without Function")
a = 1000
discount1 = 10
result1 = a - (a * discount1 / 100)

b = 2000
tax1 = 20
result2 = b + (b * tax1 / 100)
print(result1)
print(result2)

# A Code modify by function to be clean and structured
print("\nWith Function Structure")


def discount(price, discount_price):
    return price - (price * discount_price / 100)


print(discount(1000, 10))
"""
Output: 900
"""


def tax(price, amount_tax):
    return price + (price * amount_tax / 100)


print(tax(2000, 10))
"""
Output: 2200
"""

print("\nfunction that calculate discount,tax,payment")


def calculate_discount(price, discount_percent):
    return price - (price * discount_percent / 100)


def calculate_tax(price, tax_percent):
    return price + (price * tax_percent / 100)


def calculate_payment(price, discount_percent, tax_percent):
    after_dissccount = calculate_discount(price, discount_percent)
    after_tax = calculate_tax(after_dissccount, tax_percent)
    return after_tax


print(calculate_payment(2000, 20, 10))
