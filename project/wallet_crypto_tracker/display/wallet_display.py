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
    print("==== ALL USERS ====")

    for user in wallets:
        display_multiple_wallets(user)