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

    if not (valid_tx_type and valid_amount and valid_date and valid_sufficient_balance):
        validators = {
            "tx_type" : (not valid_tx_type, "TRANSACTION TYPE: Must be In or Out"),
            "amount": (not valid_amount, "AMOUNT: cant be zero, just positive"),
            "date": (not valid_date, "DATE: Only date format: YYYY-MM-DD"),
            "sufficient_balance": (not valid_sufficient_balance, "BALANCE: Insufficient balance")
        }
        for _, (is_error,error_msg) in validators.items():
            if is_error:
                return (False,error_msg)
            
    # Calculate Wallet next ID Transaction
    if not found_wallet["transaction"]: 
        tx_id = 1 # First transaction ID strat from 1
    else:
        max_id = 0 # Strart tracking from 0
        for tx in found_wallet["transaction"]: 
            if tx["tx_id"] > max_id: # If found ID than greater
                max_id = tx["tx_id"] # Update max id
        tx_id = max_id +1 

    #  Transaction Structure

    new_transaction = {
        "tx_id" : tx_id,
        "type" : tx_type,
        "amount" : amount,
        "date" : date,
        "description" : description
    }

    found_wallet["transaction"].append(new_transaction)
    return (True,f"Transaction Success added, Transaction id: {tx_id}")
        
# Calculate wallet balance from transaction
def get_wallet_balance(wallet):
    balance = 0.0
    for tx in wallet["transaction"]:
        if tx["type"] == "in":
            balance += tx["amount"]
        if tx["type"] == "out":
            balance -= tx["amount"]
    return balance

# A function who get transaction by wallet ID
def get_transaction(username,wallet_id,users_list):
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
            return wallet["transaction"]
        
    return (False, "Wallet Not Found")

# A funnction who filter transaction by type
def filter_transactions_by_type(username,wallet_id,tx_type,users_list):
    history_trx = get_transaction(username,wallet_id,users_list)
    
    filtered = []
    for tx in history_trx:
        if tx["type"] == tx_type:
            filtered.append(tx)
    return (True, filtered)

