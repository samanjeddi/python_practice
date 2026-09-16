number = int(input("number: "))

if number > 0 and number % 2 == 0:
    print("positive even")

elif number > 0 and number % 2 != 0:
    print("positive odd")

elif number < 0 and number % 2 == 0:
    print("negative even")

elif number < 0 and number % 2 != 0:
    print("negative odd")

else:
    print("zero")