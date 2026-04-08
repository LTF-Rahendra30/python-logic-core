# Module 4 Practice Nested Loop

# ===========================
# Practice 1 Simple Grid
# ===========================

print("Practice 1")
for i in range(2):
    for j in range(3):
        print(i, j)

print("\n")

# ===========================
# Practice 2 Star Pattern
# ===========================

print("Practice 2")
for row in range(4):
    for col in range(4):
        print("#", end=" ")
    print()

print("\n")

# ===========================
# Practice 3 Number Pattern
# ===========================

print("Practice 3")

for i in range(1, 4):
    for j in range(4):
        print(i, end=" ")
    print()

print("\n")

# ===========================
# Practice 4 Blockchain Analogy
# ===========================

print("Practice 4")

blockchain = [["tx1", "tx2"], ["tx3", "tx4"], ["tx5", "tx6"]]

for block in blockchain:
    for tx in block:
        print(tx)
