"""
A Simple Register Account
"""

users = []  # Global Variabels


# Formating Username Function
def normalize_username(username):
    username = username.strip().lower()
    return username


# Formating Email Function
def formatting_email(email):
    return "@" in email


# Formating Password Function
def password_check(password):
    return len(password) >= 8


# Check duplicate Username
def username_check(username, user_list):
    for u in user_list:
        if u["name"] == username:
            return False
    return True


# Check Duplicate Email
def check_email(email, user_list):
    for eml in user_list:
        if eml["email"] == email:
            return False
    return True


# Main Function
def register(username, email, password, user_list):
    username_avaliable = username_check(username, user_list)
    pwd_valid = password_check(password)
    email_format_valid = formatting_email(email)
    email_avaliable = check_email(email, user_list)

    # Valid Inputs
    if pwd_valid and username_avaliable and email_format_valid and email_avaliable:
        user_list.append({"name": username, "email": email, "password": password})
        return True, " Successed register!"

    # Eror Handling by dictionary structure
    else:
        validation = {
            "email_format": (not email_format_valid, "Plase, write with '@' "),
            "email_valid": (not email_avaliable, "Email is registered!"),
            "username_avaliable": (not username_avaliable, "Username is registered"),
            "password_valid": (
                not pwd_valid,
                "The Password must be greater than 8 character",
            ),
        }
        for _, (is_eror, eror_msg) in validation.items():
            if is_eror:
                return False, eror_msg


# Call Function
print(register("user1", "john@mail.com", "secret123", users))
print(register("user1", "john@mail.com", "secret123", users))
print(register("user1", "john@mail.com", "secret123", users))
print(users)

"""
(True, ' Successed register!')
(False, 'Email is registered!')
(False, 'Username is registered')
[{'name': 'user1', 'email': 'john@mail.com', 'password': 'secret123'}]
"""
