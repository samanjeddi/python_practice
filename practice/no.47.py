password = "python123"
count = 0

while count < 3:
    num = input("password: ")
    count += 1

    if num == password:
        print("access granted")
        break

if count == 3 and num != password:
    print("account locked")