
# Import validators function
from validators import (
    validate_username,
    validate_email,
    validate_password,
    check_email_duplicate,
    check_username_duplicate,
)

# Import clean display
from display import display_single_user,display_multiple_users
users = []  # Global data


# Register Function
def register_user(username, email, password, users_list):
    clean_username = username.strip().lower()
    username_valid = validate_username(clean_username)
    username_check = check_username_duplicate(clean_username, users_list)
    email_format = validate_email(email)
    email_check = check_email_duplicate(email, users_list)
    password_valid = validate_password(password)

    # Validate if all function conditional is True
    if (
        username_valid
        and username_check
        and email_format
        and email_check
        and password_valid
    ):
        new_user = {
            "username" : clean_username,
            "email" : email,
            "password": password,
            "wallets" : [] # User wallet
        }
        # Append user in users list 
        users_list.append(new_user)

        return True, f"Succesed Register! Welcome {clean_username}"
    else:
        validators = {
            "username_duplicate": (not username_check, "The Username has been registered! "),
            "email_valid" : (not email_format, "Please write email  with '@' "),
            "email_duplicate": (not email_check, "The email  has been registered! "),
            "password_format": (not password_valid, "The password must be at least 8 character ")
        }
        for _, (is_error,error_msg) in validators.items():
            if is_error:
                return False ,error_msg

# Get user by username
def get_user_by_username(username,users_list):
    print("================================")
    print(f"Get user by username: {username}")
    clean_username = username.lower().strip()
    result = []

    for user in users_list:
        if user["username"] == clean_username:
            result.append(user)
    if result:
        return True, display_single_user(user)
    else:
        return False, f"Not users found for username {clean_username}"
        

# Get All Users
def get_all_users(users_list):
    return display_multiple_users(users_list)