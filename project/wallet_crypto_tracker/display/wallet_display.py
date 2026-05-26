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
