from validators import validate_wallet_address,validate_balance,validate_coin_type,check_wallet_duplicate

from datetime import date

# Add wallet
def add_wallet(username,coin_type,address,users_list):

    # Find User
    clean_username = username.lower().strip()
    found_user = None

    for user in users_list:
        if user["usernname"] == clean_username:
            found_user = user
            break

    else:
        return (False, f"User {clean_username} not found")

    # Validate  Wallet
    coin_valid = validate_coin_type(coin_type)
    valid_wallet_address = validate_wallet_address(address)
    wallet_duplicate = check_wallet_duplicate(address,users_list)

    if not (coin_valid and valid_wallet_address and wallet_duplicate):
        validators = {
            "coin_type" : (not coin_valid, "Invalid coin type, Use: (Bitcoin,Ethereum,Solana)"),
            "address": (not valid_wallet_address, "Address must be at least 20 character"),
            "duplicate": (not wallet_duplicate, "Addres alredy register") 
        }
        for _,(is_error,error_msg) in validators:
            if is_error:
                return (False,error_msg)
            
        # Calculate next wallet id
    if not found_user["wallets"]:
        next_id = 1
    else:
        max_id = 0
        for wallet in found_user["wallets"]:
            if wallet["wallet_id"] > max_id:
                max_id = wallet["wallet_id"]
        next_id = max_id +1
    
        # Wallet Data Stucture:
    new_wallet = {
        "wallet_id" : next_id,
        "coin_type": coin_type,
        "address" : address,
        "balance" : 0.0,
        "create_date": str(date.today()),
        "transaction": []
    }

    found_user["wallets"].append(new_wallet)
    return (True, f"{coin_type} wallet added to {clean_username}")



