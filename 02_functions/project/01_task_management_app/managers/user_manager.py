from validators import (
    validate_username,
    validate_email,
    validate_password,
    check_email,
    check_username,
)

users = []  # Globa Users List Variabel


# Register Function
def register_user(username, email, password, users_list):
    clean_username = username.lower()
    username_format_valid = validate_username(clean_username)
    username_available = check_username(clean_username, users_list)
    email_format_valid = validate_email(email)
    email_available = check_email(email, users_list)
    pwd_format_valid = validate_password(password)

    if (
        email_format_valid
        and email_available
        and pwd_format_valid
        and username_format_valid
        and username_available
    ):
        users_list.append(
            {"name": clean_username, "email": email, "password": password}
        )

        return True, "Successed Register, WELCOME!!"

    else:
        validators = {
            "email_valid": (not email_available, "Email is Registered!"),
            "email_format": (not email_format_valid, "Plase, writwe  with '@"),
            "username_valid": (not username_available, "Username is Registered!"),
            "username_format": (
                not username_format_valid,
                "The username can't be empty",
            ),
        }
        for _, (is_error, error_msg) in validators.items():
            if is_error:
                return False, error_msg


# Get a All Users who Success Registered
def get_users(users_list):
    return users_list


# Get User by Username
def get_user_by_username(username, users_list):
    clean_username = username.lower()
    for usr in users_list:
        if usr["name"] == clean_username:
            return True
    return False, "Username not Registered! "
