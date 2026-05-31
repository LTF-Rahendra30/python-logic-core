
from managers import (
    # Register
    register_user,get_user_by_username,get_all_users,users,
    
    # Wallet Managers
    add_wallet,get_wallets_by_user,get_wallet_by_id,calculate_user_total_balance,

    # Transaction Managers
    add_transaction,get_transaction,filter_transactions_by_type,filter_transactions_by_date,filter_transaction_by_hash
    )


def main():
    print(register_user("Bob","Bob@mail.com","joko1234567",users))

    print("\n" + "=" * 50 + "\n")

    # Add wallet
    print(add_wallet("bob","BITCOIN","11bbabbc213370099effb32bfe31699",users))
    print(add_wallet("bob","solana","22eeb3987abe3345cc231fffcdee337efb2",users))

    print("\n" + "=" * 50 + "\n")

    # Add transaction
    print(add_transaction("bob",1,"in",0.1,"From CEX","2026-05-21",users))
    print(add_transaction("bob",1,"in",1,"From CEX","2026-05-25",users))
    print(add_transaction("bob",1,"out",0.5,"Send to dony","2026-05-31",users))
    print(add_transaction("bob",2,"in",0.3,"from dony","2026-05-31",users))

    print("\n" + "=" * 50 + "\n")

    # Get Data
    get_wallets_by_user("bob",users)
    get_transaction("bob",2,users)
    filter_transactions_by_type("bob",1,"out",users)
    filter_transaction_by_hash("bob","0x8a665ce8c4a01aebf6c6c3c4a5d5eab50b3cfdb4b1e419c46e383a22ecd35b3f",users)

    # Calculate total balace
    print(calculate_user_total_balance("bob",users))

if __name__ == "__main__":
    main()