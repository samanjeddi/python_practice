password = "python123"
a = input("password: ")

while a != password:
    print("wrong password")
    a = input("password: ")

    if a == password:
        print("great")
    