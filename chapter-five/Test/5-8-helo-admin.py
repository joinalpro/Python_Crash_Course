# usernames = ['admin', 'jaden','joinal','nasir','forhad']
# if 'admin' in usernames:
#     print("Hello admin, would you like to see a status report?")
# if 'jaden' in usernames:
#     print("Hello Jaden, thank you for logging in again.")
usernames = []
if usernames:
    for user in usernames:
        print(f"Adding {user}.")
    print("\nFinished adding name.")
else:
    print("list names are empty")