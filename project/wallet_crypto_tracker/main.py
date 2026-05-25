from validators.user_validators import validate_username,validate_password

from managers.user_manager import register_user,get_user_by_username,users

# print(validate_username(" "))
# print(validate_password("1231dsddsddadawd"))

print(register_user("joko","joko@mail.com","joko1234567",users))
print(register_user("WOWO","wowo@mail.com","joko1234567",users))
print("=======================")
print(get_user_by_username("joko",users))
print(get_user_by_username("WOWO",users))