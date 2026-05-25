

# Clean Display Function
def display_single_user(user):
    print(f"""Username: {user['username']} | Email: {user['email']}
Wallets: {len(user['wallets'])}
─────────────────────
""")


def display_multiple_users(users_list):
    if not users_list:
        print("No users found")
        return
    
    print("==== ALL USERS ====")

    for user in users_list:
        display_single_user(user)
