# Validators Username Func
def validate_username(username):
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


# Validators Owner Exist for Create new Task
def validate_owner_exists(owner, users_list):
    for u in users_list:
        if u["name"] == owner:
            return True
        return False


# Validators Email Exist for Create new Task
def validate_email_exists(email_owner, users_list):
    for u in users_list:
        if u["email"] == email_owner:
            return True
        return False
