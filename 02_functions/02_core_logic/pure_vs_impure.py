"""Pure Function"""


# This pure function with parameters and return result
def discount(price, discount):
    payment = price - (price * discount / 100)
    return payment


print(discount(100, 30))

"""Impure Function"""

balance = 1000  # This Default balance value


def add_balance():
    balance_input = int(input("Add your balance: "))
    total_balance = balance_input + balance
    return total_balance


print(add_balance())
"""
It dose work, but there are several things you need pay attention to:
- Too dependent on external variabel
- Side effect I/O
"""

# Pure function si predictable and easier and to test
# Impure Function can cause side effect and hidden bugs
