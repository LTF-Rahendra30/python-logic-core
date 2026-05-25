def validate_coin_type(coin_type):
    return coin_type in ["Bitcoin", "Ethereum", "Solana"]

def validate_wallet_addres(addres):
    return len(addres) >= 20

def check_wallet_duplicate(address,users_list):
    for user in users_list:
        for adrs in user["wallets"]:
            if adrs["address"] == address:
                return False
    return True

def validate_balance(balance):
    return balance > 0
            
