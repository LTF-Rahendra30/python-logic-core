def validate_tx_type(tx_type):
    return tx_type in ["in","out"]

def validate_amount(amount):
    return amount > 0

