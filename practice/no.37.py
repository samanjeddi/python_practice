username = input("username: ")
password = int(input("pawwsord: "))

correct_username = "admin"
correct_passwod = 1234

if username == correct_username and password == correct_passwod:
    print("Login Succesfull")

elif username != correct_username and password == correct_passwod:
    print("Wrong Username")

elif username == correct_username and password != correct_passwod:
    print("Wrong Password")

else:
    print("Wrong Password & Username")