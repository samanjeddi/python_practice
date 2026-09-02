x = int(input("number: "))
n = int(input("times: "))

if 0 < n < 21 and 0 < x < 1001:
    for i in range(n):
        if x % 2 == 0:
         x = x // 2
        else:
         x = 2 * x - 1
         
    print(x)
else:
    print("invalid")