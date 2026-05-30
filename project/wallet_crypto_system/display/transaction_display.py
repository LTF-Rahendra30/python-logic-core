# Display Transaction without hash
def display_single_transaction_simple(transaction):
    print(f"""
    TX ID: {transaction['tx_id']}
    Type: {transaction['type']}
    Amount: {transaction['amount']}
    Date: {transaction['date']}
    Description: {transaction['description']}
""")
    
# Display Transaction with hash
def display_single_transaction(transaction):
    print(f"""
    Transaction Hash: {transaction['transaction_hash']}
    TX ID: {transaction['tx_id']}
    Type: {transaction['type']}
    Amount: {transaction['amount']}
    Date: {transaction['date']}
    Description: {transaction['description']}
    """)

# Display multiple transaction with hash
def display_transaction_history(transaction):
    if not transaction:
        print("No transaction")
    print("=== TRANSACTION HISTORY ===\n")
    for tx in transaction:
        display_single_transaction(tx)
