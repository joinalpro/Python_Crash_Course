current_users = ['nasir','forhad','joinal', 'panu','abir']
new_users = ['nasir','abir','badon','delowar','khan']

for new_user in new_users:
    if new_user in current_users:
        print(f"Adding {new_user}.")
    else:
        print(f"{new_user} not found in current user")
print("\nFinished making your pizza.")