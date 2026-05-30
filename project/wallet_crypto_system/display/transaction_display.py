
def display_single_transaction_simple(transaction):
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
    print(f"""
    Transaction Hash: {transaction['transaction_hash']}
    TX ID: {transaction['tx_id']}
    Type: {transaction['type']}
    Amount: {transaction['amount']}
    Date: {transaction['date']}
    Description: {transaction['description']}
    """)