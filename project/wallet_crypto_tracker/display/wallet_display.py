# def display_wallet(user):
    
def display_single_wallet(wallet):
    print(f"""
     "Wallet_id": {wallet['wallet_id']},
     "Coin_type": {wallet['coin_type']},
     "Address" : {wallet['address']},
     "Balance" : {wallet['balance']},
     "Create_date": {wallet['create_date']},
     "Transaction": {wallet['transaction']}
    ____________________________
""")

def display_multiple_wallets(wallets):
    if not wallets:
        print("No wallet found")
        return
    print("==== ALL WALLETS ====")

    for wallet in wallets:
        display_single_wallet(wallet)

def display_wallet_by_id(wallet_id,wallet):
    print("================================")
    print(f"Get wallet ID: {wallet_id}")
    print("================================")
    display_single_wallet(wallet)

def display_user_total_balance(username,total_balance):
    print("================================")
    print(f"Total Balance for {username}")
    print("================================")
    print(f"Total Balance: {total_balance}")
    print("================================")


