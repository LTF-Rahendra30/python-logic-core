def display_wallet(next_id,clean_type_coin,address,balance,date,transaction):
    print(f"""

    "wallet_id": {next_id['wallet_id']},
    "coin_type": {clean_type_coin['coin_type']},
    "address" : {address['address']},
    "balance" : {balance['balance']},
    "create_date": {date['create_date']},
    "transaction": {transaction['transaction']}

""")