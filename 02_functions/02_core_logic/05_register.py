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
  return len(password) >= 8


def username_check(username):
    for u in users:
        if u["name"] == username:
            return False
    return True


def check_email(email):
  for eml in users:
    if eml["email"] == email:
      return False
  return True


def register(username, email, password,user_list):
    users = user_list
    username_format = normalize_username(username)
    pwd_valid = password_check(password)
    username_avaliable = username_check(username_format)
    email_format_valid = formatting_email(email)
    email_avaliable = check_email(email)

    if pwd_valid and username_avaliable and email_format_valid and email_avaliable:
        users.append({"name": username_format, "email": email, "password": password})
        return True, " Successed register!"
    else:
      validation = {
        "email_format" : (not email_format_valid, "Plase, write with '@' "),
        "email_valid" : (not email_avaliable,"Email is registered"),
        "username_valid" : (not username_avaliable,"Username is registered"),
        "password_valid" : (not pwd_valid,"The Password must be greater than 8 character")
      }
      for eror_key, (is_eror,eror_msg) in validation.items():
        if is_eror:
          return False, eror_msg


# Call 1
result1 = register("john", "john@mail.com", "secret123")
print(result1)  # (True, "Success")
print(users)    # [{"name": "john", ...}]  ← users BERUBAH

# Call 2 - SAMA INPUT, TAPI HASIL BEDA
result2 = register("john", "john@mail.com", "secret123")
print(result2)  # (False, "Username is registered")  ← BEDA!
print(users)    # [{"name": "john", ...}]  ← users sudah ada john