
user_list = [
    (0,"Bob","Mechanic"),
    (1,"John","Traitor"),
    (2,"Kady","Cooker"),
    (3,"Cergy","Chimist")
]

user_mapping = { user[1]: user for user in user_list }

print(user_mapping)

user_input = input("Enter your username : ")
user_password = input("Enter your password : ")


_,username,password = user_mapping[user_input]

if user_password == password:
    print("Your informations are correct")
else:
    print("Your details are wrong")