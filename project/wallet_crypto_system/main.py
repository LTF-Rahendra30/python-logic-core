
from managers import register_user,get_user_by_username,get_all_users,users

from managers import add_wallet,get_wallets_by_user,get_wallet_by_id,calculate_user_total_balance



print(register_user("joko","joko@mail.com","joko1234567",users))

print(add_wallet("joko","BITCOIN","11bbabbc213370099effb32bfe31699",users))

print(add_wallet("joko","solana","22eeb3987abe3345cc231fffcdee337efb2",users))

print(get_wallets_by_user("joko",users))


print(calculate_user_total_balance("joko",users))
