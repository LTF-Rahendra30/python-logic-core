"""
A simple blockchain mining simulation with:
- hashlib library to make simple hash sha256
- time library to make timestamp and make ETA
"""

# == Import Library Hash and Time ==

import hashlib
import time

# == Exemeples transaction data ==
transactions = [
    {"from": "A", "to": "B", "amount": 10},
    {"from": "C", "to": "D", "amount": 20},
    {"from": "E", "to": "F", "amount": -5},  # invalid
]

valid_transaction = []
invalid_transaction = []

# == Validation Transaction ==
for t in transactions:
    if t["amount"] <= 0:
        invalid_transaction.append(t)
    else:
        valid_transaction.append(t)

# == Build Block Data ==
block_data = ""
for tx in valid_transaction:
    block_data += f"{tx['from']} -> {tx['to']}: {tx['amount']} , "

# == The mining process ==

# Time Stamp
local_time = time.localtime()
time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", local_time)

# ETA
eta = time.time()
minutes = int(eta % 60)
seconds = int(eta % 60)

# Nonce and Difficutly
nonce = 0
attempt = 0
difficutly = 4
target_prefix = "0" * difficutly  # Difficutly prefix, hash must be start whit "000"

while True:
    attempt += 1

    # Merging block and nonce
    text = f"{block_data}| nonce: {nonce}"
    hash_result = hashlib.sha256(text.encode("utf-8")).hexdigest()

    if hash_result.startswith(target_prefix):
        print("\nBlock Mined!")
        print(f"Time: {time_stamp}")
        print(f"ETA ~: Confirmed {minutes} minutes {seconds} seconds")
        print(f"Valid transaction data: {text}")
        print(f"Hash: {hash_result}")
        print(f"Nonce: {nonce}")
        print(f"Attempt: {attempt}")
        break

    nonce += 1
