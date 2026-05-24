
def validate_email(email):
    return "@" in email

def validate_username(username):
    return username not in [""," "]

def validate_password(password):
    return len(password) >=8

def check_username_duplicate(username,users_list):
    for usr in users_list:
        if usr["name"] == username:
            return False
    return True

def check_email_duplicate(email,users_list):
    for eml in users_list:
        if eml["email"] == email:
            return False
    return True

