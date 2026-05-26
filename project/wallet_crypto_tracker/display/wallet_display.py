def display_wallet(user):
    print(f"""

    "wallet_id": {user['wallet_id']},
    "coin_type": {user['coin_type']},
    "address" : {user['address']},
    "balance" : {user['balance']},
    "create_date": {user['create_date']},
    "transaction": {user['transaction']}

""")