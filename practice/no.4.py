total = 0

while True:
    number = int(input("enter a number: "))

    if number == 0:
        break

    elif number < 0:
        continue

    total += number

print("sum:", total)