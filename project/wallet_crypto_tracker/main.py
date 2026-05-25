from validators.user_validators import validate_username,validate_password

from managers.user_manager import register_user,get_user_by_username,get_all_users,users

from managers import add_wallet,get_wallets_by_user
# print(validate_username(" "))
# print(validate_password("1231dsddsddadawd"))

print(register_user("joko","joko@mail.com","joko1234567",users))
print(add_wallet("joko","Bitcoin","11bbabbc213370099effb32bfe31699",users))
print(add_wallet("joko","Bitcoin","22eeb3987abe3345cc231fffcdee337efb2",users))
print(get_wallets_by_user("joko",users))

