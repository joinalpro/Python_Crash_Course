banned_users = ['andrew', 'carolina', 'david']
# user = 'marie
user_two = 'david'
if user_two not in banned_users:
    print(f"{user_two.title()}, you can post a response if you wish.")
else:
    print("you are banned")