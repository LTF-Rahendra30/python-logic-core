from validators import validate_wallet_address,validate_balance,validate_coin_type,check_wallet_duplicate

from validators import check_username_duplicate,validate_username


# Add wallet
def add_wallet(username,coin_type,address,users_list):

    # Find User
    clean_username = username.lower().strip()
    username_valid = validate_username(clean_username)
    username_duplicate = check_username_duplicate(clean_username, users_list)
    

    
        # Wallet Data Stucture:
        new_wallet = {
            "wallet_id" : 
        }




    coin_valid = validate_coin_type(coin_type)
    valid_wallet_address = validate_wallet_address(address)
    wallet_duplicate = check_wallet_duplicate(address,users_list)