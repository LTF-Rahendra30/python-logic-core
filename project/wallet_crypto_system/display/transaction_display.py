def display_single_transaction(transaction):
    print(f"""
    Transaction Hash: {transaction['transaction_hash']}
    TX ID: {transaction['tx_id']}
    Type: {transaction['type']}
    Amount: {transaction['amount']}
    Date: {transaction['date']}
    Description: {transaction['description']}
""")