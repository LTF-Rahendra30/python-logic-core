from validators import (
    validate_username,
    validate_email,
    validate_password,
    check_email,
    check_username,
)

from managers.clear_users_display import clean_display_user, display_multiple_users

users = []  # Globa Users List Variabel


# Register Function
def register_user(username, email, password, users_list):
    clean_username = username.lower().strip()
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

        return True, f"Successed Register, WELCOME!! {clean_username
}"
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
    print("Get All Users who Successed registered")
    display_multiple_users(users_list)


# Get User by Username
def get_user_by_username(username, users_list):
    print(f"Get user by username: {username}")
    clean_username = username.lower().strip()
    result = []
    for usr in users_list:
        if usr["name"] == clean_username:
            result.append(usr)
    if result:
        display_multiple_users(result)
    else:
        print(f"Not users found for username {clean_username}")
