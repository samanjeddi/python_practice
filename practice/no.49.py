def check_number(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("number: "))
a = check_number(num)
print(a)