# Copyright 2026 LTF30

"""
Module 03 Practice
Enumerate Usage


Practice sessions to understand how enumerate() works
with index and values during iteration.
"""


# ==============================
# Practice 1 — Basic Enumerate
# ==============================


print("Practice 1 — Basic Enumerate")


fruits = ["apple", "banana", "mango", "orange"]


for index, fruit in enumerate(fruits):
    print(index, fruit)


print("\n----------------\n")


# ==============================
# Practice 2 — Start Index
# ==============================


print("Practice 2 | Start Index")


animals = ["cat", "dog", "rabbit","horse","tiger"]


for number, animal in enumerate(animals, start=1):
    print(number, animal)


print("\n----------------\n")


# ==============================
# Practice 3 — Formatting Output
# ==============================


print("Practice 3 | Formatting Output")


students = ["Ali", "Budi", "Citra"]


for i, student in enumerate(students, start=1):
    print(f"Student {i} -> {student}")


print("\n----------------\n")


# ==============================
# Practice 4 — Simple Crypto Example
# ==============================


print("Practice 4 | Transaction List")


transactions = [
    "0xa1f4",
    "0xb9c2",
    "0xf331",
    "0x91af"
]

for index, tx in enumerate(transactions, start=1):
    print(f"Transaction {index} : {tx}")

print("\n----------------\n")

# ==============================
# Practice 5 — Multiply Value
# ==============================


print("Practice 5 | Repeat Value")


coins = ["btc","eth","sol","bnb","tron","hype"]


for i, coin in enumerate(coins, start=1):
    print(i, coin.upper())