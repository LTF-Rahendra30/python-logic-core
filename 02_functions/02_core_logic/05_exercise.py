"""
Simple Register Account
"""

users = []


def normalize_username(username):
    username = username.strip().lower()
    return username


def formatting_email(email):
    return "@" in email


def password_check(password):
    if len(password) < 8:
        return False
    return True


def username_check(username):
    for u in users:
        if u["name"] == username:
            return False
    return True


# def check_email(email):
#     for eml in users:
#         if eml["email"] == email:
#             return False
#     return True


def register(username, email, password):
    pwd_valid = password_check(password)
    username_avaliable = username_check(username)
    email_format_valid = formatting_email(email)

    if pwd_valid and username_avaliable and email_format_valid:
        users.append({"name": username, "email": email, "password": password})
        return True, " Successed register!"
    else:
        if not pwd_valid:
            return False, "The Password must be greater than 8 character"
        elif not username_avaliable:
            return False, "Username is registered"
        elif not email_format_valid:
            return False, "Plase, write with '@' "


print(register("JOKO", "JOKO@gmail.com", "123456joko"))
print(register("wowo", "JOKOgmail.com", "123456joko"))
print(users)
