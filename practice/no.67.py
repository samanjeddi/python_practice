def sum_numbers(*args):
    totall = 0
    for a in args:
        totall += a
    return totall

a = int(input("first number: "))
b = int(input("second number: "))
c = int(input("third number: "))

nums = sum_numbers(a, b, c)
print(nums)