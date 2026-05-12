# Validators Username Func
def validate_username(username):
    username = username.lower()
    return username not in ["", " "]


# Validators Email Func
def validate_email(email):
    return "@" in email


# Validators Passowrd Func
def validate_password(password):
    return len(password) >= 8


# Validators Duplicate Username
def check_username(username, username_list):
    for u in username_list:
        if u["name"] == username:
            return False
    return True


print(validate_username("HIHIHI"))
