
from managers import register_user,get_user_by_username,get_all_users,users

from managers import add_wallet,get_wallets_by_user,get_wallet_by_id,calculate_user_total_balance

from managers import add_transaction,get_transaction,filter_transactions_by_type,filter_transactions_by_date,filter_transaction_by_hash

print(register_user("joko","joko@mail.com","joko1234567",users))

print(add_wallet("joko","BITCOIN","11bbabbc213370099effb32bfe31699",users))

print(add_wallet("joko","solana","22eeb3987abe3345cc231fffcdee337efb2",users))

print(add_transaction("joko",1,"in",0.1,"From CEX","2026-05-21",users))
print(add_transaction("joko",1,"in",1,"From CEX","2026-05-25",users))
print(add_transaction("joko",1,"out",0.5,"Send to bahlil","2026-05-31",users))
print(add_transaction("joko",2,"in",0.3,"from bahlil","2026-05-31",users))
print(get_wallets_by_user("joko",users))
print(filter_transaction_by_hash("joko","0x0e11c5342cebce8f713f6fcf81aebc48dfcdf66c3fca074af4fb64058b78417c",users))


# print(calculate_user_total_balance("joko",users))
# print(get_transaction("joko",2,users))
# print(filter_transactions_by_type("joko",1,"out",users))
