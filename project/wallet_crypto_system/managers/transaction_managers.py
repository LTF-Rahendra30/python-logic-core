import hashlib

from typing import Tuple, Any # Import tuple class

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
    found_wallet = None
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


    # Encryption Transaction Data with sha256 before append new transacction

    data_transaction = f"{username}, {wallet_id},{tx_type}, {amount}, {description}, {date}"

    hash_transaction = f"0x{hashlib.sha256(data_transaction .encode('utf-8')).hexdigest()}"

    #  Transaction Structure
    new_transaction = {
        "transaction_hash": hash_transaction,
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
def get_transaction(username,wallet_id,users_list) -> Tuple[bool,Any]:
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
    found_wallet = None
    for wallet in found_user["wallets"]:
        if wallet["wallet_id"] == wallet_id:
            found_wallet = wallet
            break
    if found_wallet is None:
        return (False, "Wallet Not Found")
    
    return(True,found_wallet["transaction"])

# A funnction who filter transaction by type
def filter_transactions_by_type(username,wallet_id,tx_type,users_list):
    success, history_trx = get_transaction(username,wallet_id,users_list)

    if not success:
        return (False, history_trx)

    filtered_type = []
    for tx in history_trx:
        if tx["type"] == tx_type:
            filtered_type.append(tx)
    return (True, f"Transaction by type: {tx_type}: ",filtered_type)

# A function who filtered by date
def filter_transactions_by_date(username,wallet_id,start_date,end_date,users_list):
    # Get transaction history
    success, history_trx = get_transaction(username,wallet_id,users_list)

    if not success:
        return (False, history_trx)
    
    filtered_date = []
    for tx in history_trx:
        if start_date <= tx["date"] <= end_date:
            filtered_date.append(tx)
    return (True, f"Transaction by date {start_date} to {end_date}: {filtered_date}")
            
# A function who filtered transaction by hash
def filter_transaction_by_hash(username,hash_transaction,users_list):
    clean_username = username.strip().lower()
    found_user = None
    # Find username
    for user in users_list:
        if user["username"] == clean_username:
            found_user = user
            break
    
    if found_user is None:
        return (False, f"User {clean_username} not found")
    # Found wallet
    for wallet in found_user["wallets"]:
        # Found Transaction by transaction hash match
        for trx in wallet["transaction"]:
            if trx["transaction_hash"] == hash_transaction:
                found_transaction = trx
                return(True,found_transaction)
    return (False, "Transaction not found")



