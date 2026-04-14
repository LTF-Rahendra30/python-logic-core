"""
Part 1 Accumulator Algorthmic
Used loop for solved specific problem, main focus is a collect value
"""

number = [10, 20, 30]

total = 0  # Accumulator

for n in number:
    total += n
print(f"\nTotal: {total}")

"""
The output like this:

60 
    
    ---> Why?? Why can it be 60?

Explanations:

Oke a right, number var have a this velue [10,20,30]
and the accumulator is the default steatment.

The loop on part (n.... in... number) that is loop each value on number variables
and the opration (total += n) that is a addition operator, so every value on variables number [10,20,30]
will be added with prevoius velue of the variables, like this:

10+0 = 10
10+20 = 30
30+30 = 60

So, Ezy to understand right??
like as aritmatic operation, Hahaha

"""
# Real Case Example on the total balance in the  wallet crypto

coin_ownerShip = {"BITCOIN": 1000, "ETHEREUM": 2000, "BNB": 3000, "SOLANA": 4000}

total = 0

for balance in coin_ownerShip.values():
    total += balance
print(f"\nOwnership: {coin_ownerShip}")
print(f"\nBalance Coin: {total}")
