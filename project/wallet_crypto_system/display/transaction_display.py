
def display_single_transaction(transaction):
    print(f"""
    TX ID: {transaction['tx_id']}
    Type: {transaction['type']}
    Amount: {transaction['amount']}
    Date: {transaction['date']}
    Description: {transaction['description']}
""")
    
def display_transaction_history(transaction):
    if not transaction:
        print("No transactions")
    
    print("=== TRANSACTION HISTORY ===\n")
    for tx in transaction:
        print(f"""
    Transaction Hash: {transaction['transaction_hash']}
    TX ID: {transaction['tx_id']}
    Type: {transaction['type']}
    Amount: {transaction['amount']}
    Date: {transaction['date']}
    Description: {transaction['description']}
    """)