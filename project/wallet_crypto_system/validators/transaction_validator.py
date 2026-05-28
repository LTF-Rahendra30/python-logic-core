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
    if len(part[0]) != 4 or len(part[1]) != 2 or len(part[2]) != 2:
        return False
    
    return True