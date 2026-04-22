"""
The Simple Blockchain Ledger Simulation
This project simulations a transaction ledger using basic Python
"""

# Example Transaction Data
transactions = [150, -20, 300, -50, 0, 700, -300, 1200, -10, 50, -700, 400, 0, -5, 900]

# === DISPLAY ALL TRANSACTIONS ===
print("=== DISPLAY ALL TRANSACTIONS ===")

for tx in transactions:
    print(tx)

# === ENUMERATE ALL TRANSACTIONS ===
print("\n=== ENUMERATE TRANSACTIONS ===")

for index, tx in enumerate(transactions, start=1):
    print(f"Transaction Data {index}:", tx)


# === FILTERING VALID TRANSACTIONS ===
print("\n=== FILTERING TRANSACTIONS ===")

for tx in transactions:
    if tx > 0:
        print(f"Valid transaction: {tx} ")


# === CALCULATE TOTAL BALANCE TRANSACTIONS ===
print("\n=== BALANCE TRANSACTIONS ===")

balance = 0
for tx in transactions:
    if tx > 0:
        balance += tx
print(f"Total Balance: {balance}")


# === FIND MAX TRANSACTIONS ===
print("\n=== MAX TRANSACTIONS ===")

max_tx = transactions[0]

for tx in transactions:
    if tx > max_tx:
        max_tx = tx
print(f"Max Transaction {max_tx}")


# === BLOCK SIMULATION ===

blocks = [
    [150, -20, 300],
    [-50, 700, -300],
]

balance = 0

print("\n=== Block Access ===")
for block_index, the_block in enumerate(blocks, start=1):
    print(f"\nData Block Transactions {block_index}: {the_block}")

    for tx_index, tx in enumerate(the_block, start=1):
        print(f"Value Transaction {tx_index}: {tx}")
