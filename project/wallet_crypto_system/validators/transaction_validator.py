def validate_tx_type(tx_type):
    return tx_type in ["in","out"]

def validate_amount(amount):
    return amount > 0

def validate_date(date):
    parts = date.split("-")

    #  Check lenght
    if len(parts) !=3:
        return False
    
    # Check digit
    for part in parts:
        if not part.isdigit():
            return False
        
    # Check date  format
    if len(parts[0]) != 4 or len(parts[1]) != 2 or len(parts[2]) != 2:
        return False
    
    return True

def validate_sufficient_balance(tx_type,amount,wallet):
    if tx_type == "in":
        return True
    
    
    current_balance = 0.0
    for tx in wallet["transaction"]:
        if tx["type"] == "in":
            current_balance += amount
        else:
            current_balance -= amount
    return current_balance >= amount