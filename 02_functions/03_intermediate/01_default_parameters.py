# Default Parameters

# Default parameters allow a function to have fallback values
# when no argument is provided.


# Example
def tax_calculation(price, tax=0):
    result = price + (price * tax)
    return result


# Usage
print(tax_calculation(10000))  # no tax
print(tax_calculation(20000, 10))  # with tax

"""
The output:
10000.0  # no tax
22000.0  # with tax

The default parameters make functions flexible 
Avoid repeating common values
"""
