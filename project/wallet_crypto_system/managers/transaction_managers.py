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
            return (True,wallet)
        else:
            return (False, "Wallet Not Found")

    # Transaction Data
    valid_tx_type = validate_tx_type(tx_type) 

        
