n = int(input("write a number: "))
print(n)

if 2 <= n <= 1000:
    while n != 1:
        if n % 2 == 0:
            print(n)
            n = n // 2
        else:
            print(n)
            n = (n * 3) + 1
else:
    print("your number is not valid.")