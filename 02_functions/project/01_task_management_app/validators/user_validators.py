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
def check_username(username, users_list):
    for u in users_list:
        if u["name"] == username:
            return False
    return True


# Validators Duplicate Email
def check_email(email, users_list):
    for eml in users_list:
        if eml["email"] == email:
            return False
    return True
