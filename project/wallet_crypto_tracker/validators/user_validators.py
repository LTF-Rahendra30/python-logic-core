
def validate_email(email):
    return "@" in email

def validate_username(username):
    return username not in [""," "]

def validate_password(password):
    return len(password) >=8