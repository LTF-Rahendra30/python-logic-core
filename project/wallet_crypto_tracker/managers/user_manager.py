from validators import (
    validate_email,
    validate_password,
    check_email_duplicate,
    check_username_duplicate,
)

users = []  # Global data


# Register Function
def register_user(username, email, password, users_list):
    clean_username = username.strip().lower()
    username_check = check_username_duplicate(username, users_list)
    email_format = validate_email(email)
    email_check = check_email_duplicate(email, users_list)
    password_valid = validate_password(password)

    # Validate if all function conditional is True
    if (
        clean_username
        and username_check
        and email_format
        and email_check
        and password_valid
    ):
        # Append user in users list 
        users_list.append(
            {
                "username": clean_username,
                "email": email_format,
                "password": password_valid,
            }
        )
        return True, f"Succesed Register! Welcome {clean_username}"
    else:
        validators = {
            "username_duplicate": (not username_check, "The Username has been registered! "),
            "email_valid" : (not email_format, "Please write email  with '@' "),
            "email_duplicate": (not email_check, "The email  has been registered! "),
            "password_format": (not password_valid, "The password must be at least 8 character ")
        }
        for _, (is_error,error_msg) in validators:
            if is_error:
                return False ,error_msg

