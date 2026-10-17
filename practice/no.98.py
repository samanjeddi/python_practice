user_name = input("username: ")
password = int(input("password: "))

re_user_name = input("username again: ")
re_password = int(input("password again: "))

if user_name != re_user_name:
    print("user not found")

elif password != re_password:
    print("incorrect password")

else:
    print("successful login")