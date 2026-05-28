from validators import (
    validate_tx_type,
    validate_amount,
    validate_sufficient_balance,
    validate_date,
)


def add_transaction(
    username, wallet_id,tx_type, amount, description, date, users_list
):
    clean_username = username.strip().lower()
    found_user = None
    # Find username
    for user in users_list:
        if user["username"] == clean_username:
            found_user = user
            break
    
    if found_user is None:
        return (False, f"User {clean_username} not found")
    
    # Find wallet
    for wallet in found_user["wallets"]:
        if wallet["wallet_id"] == wallet_id:
            found_wallet = wallet
            break
    if found_wallet is None:
        return (False, "Wallet Not Found")

    # Transaction Data validator
    valid_tx_type = validate_tx_type(tx_type)
    valid_amount = validate_amount(amount)
    valid_date = validate_date(date)
    valid_sufficient_balance = validate_sufficient_balance(tx_type,amount,wallet)

    if not valid_tx_type and valid_amount and valid_date and valid_sufficient_balance:
        validators = {
            "tx_type" : (not valid_tx_type, "Must be In or Out"),
            "amount": (not valid_amount, "cant be zero, just positive"),
            "date": (not valid_date, "Only date format: YYYY-MM-DD"),
            "sufficient_balance": (not valid_sufficient_balance, "Insufficient balance")
        }
        for _, (is_error,error_msg) in validators.items():
            if is_error:
                return False,error_msg
            


        
