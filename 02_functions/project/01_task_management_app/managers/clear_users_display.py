# Clean Display Users
def clean_display_user(user):
    print(f"""
"Name": {user['name']}
"Email": {user['email']}
"Password": {user['password']} \n""")


def display_multiple_users(user_list):
    if not user_list:
        print("User not found")
        return
    for user in user_list:
        clean_display_user(user)
