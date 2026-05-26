from validators import validate_wallet_address,validate_balance,validate_coin_type,check_wallet_duplicate

from display import display_single_wallet,display_user_total_balance,display_wallet_by_id,display_multiple_wallets

from datetime import date

# Add wallet
def add_wallet(username,coin_type,address,users_list):

    # Find User
    clean_username = username.lower().strip()
    found_user = None

    for user in users_list:
        if user["username"] == clean_username:
            found_user = user
            break

    if found_user is None:
        return (False, f"User {clean_username} not found")

    # Validate  Wallet
    clean_type_coin = coin_type.upper().strip()
    coin_valid = validate_coin_type(clean_type_coin)
    valid_wallet_address = validate_wallet_address(address)
    wallet_duplicate = check_wallet_duplicate(address,users_list)

    if not (coin_valid and valid_wallet_address and wallet_duplicate):
        validators = {
            "coin_type" : (not coin_valid, "Invalid coin type, Use: (Bitcoin,Ethereum,Solana)"),
            "address": (not valid_wallet_address, "Address must be at least 20 character"),
            "duplicate": (not wallet_duplicate, "Addres alredy register") 
        }
        for _,(is_error,error_msg) in validators.items():
            if is_error:
                return (False,error_msg)
            
    # Calculate next wallet id Wallet ID Number
    if not found_user["wallets"]: 
        next_id = 1 # First wallet strat from 1
    else:
        max_id = 0 # Strart tracking from 0
        for wallet in found_user["wallets"]: 
            if wallet["wallet_id"] > max_id: # If found ID than greater
                max_id = wallet["wallet_id"] # Update max id
        next_id = max_id +1 

        """
        [wallet_id:1, wallet_id:2, wallet_id:5]
         ↑           ↑           ↑
         0 < 1       1 < 2       2 < 5
         max_id=1    max_id=2    max_id=5

        next_id = 5 + 1 = 6
        """
    
        # Wallet Data Stucture:
    new_wallet = {
        "wallet_id" : next_id,
        "coin_type": clean_type_coin,
        "address" : address,
        "balance" : 0.0,
        "create_date": str(date.today()),
        "transaction": []
    }

    found_user["wallets"].append(new_wallet)
    return (True, f"{clean_type_coin} wallet added to {clean_username}")


# Get wallet by Username
def get_wallets_by_user(username,users_list):
    clean_username = username.lower().strip()

    print("================================")
    print(f"Get wallet by username: {clean_username}")

    found_user = None
    for user in users_list:
        if user["username"] == clean_username:
            found_user = user
            break
    if found_user is None:
        return (False, f"Wallets by user: {clean_username} not found")

    # Display Multiple wallets
    return display_multiple_wallets(found_user["wallets"])


# Get wallet by ID
def get_wallet_by_id(username,wallet_id,users_list):
    clean_username = username.lower().strip()
    print("================================")
    print(f"Get wallet by Username: {clean_username} ID: {wallet_id}")

    # User chek, whether there is or not
    found_user = None
    for user in users_list:
        if user["username"] == clean_username:
            found_user = user
            break
            
    if found_user is None:
        return (False, f"Wallets by user: {clean_username} not found")
    
    # Wallet ID chek, whether there is or not
    for wallet in found_user["wallets"]:
        if wallet["wallet_id"] == wallet_id:
            return display_wallet_by_id(wallet_id,wallet)
    return False, "Not found!"

# Calculate total balance wallet
def calculate_user_total_balance(username,users_list):
    clean_username = username.lower().strip()
    print("================================")
    print(f"Total Balance wallet by username: {clean_username}")

    # User chek, whether there is or not
    found_user = None
    for user in users_list:
        if user["username"] == clean_username:
            found_user = user
            break
            
    if found_user is None:
        return (False, f"Wallets by user: {clean_username} not found")
    
    # Calculate total balance
    total_balance = 0.0
    for wallet in found_user["wallets"]:
        total_balance += wallet["balance"]
    return display_user_total_balance(clean_username,total_balance)
