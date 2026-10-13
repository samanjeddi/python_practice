def plus_from_zero(n):
    totall = 0
    for num in range(0, n+1):
        totall += num
        print(num, end="\t")

    print()
    print(f"totall: {totall}")

num = int(input("number: "))
plus_from_zero(num)