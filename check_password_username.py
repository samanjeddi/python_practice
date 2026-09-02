user_name = input("user name: ")
password = input("password: ")

if len(user_name) < 3:
    print("Error , your user name should be more than 3 characters.")
else:
    print(f"your user name is {user_name}.")

if len(password) < 8:
    print("Error , your password should be more than 8 characters.")

has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break
if has_digit == False:
    print("your password need at least 1 number.")

has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break
if has_upper == False:
    print("your password need at least 1 upper character.")
    
else:
    print(f"your password is {password}.")