a = int(input("write a range: "))

for n in range(a):
    n += 1
    if n % 3 == 0 and n % 5 == 0:
        print("hiphop")
        continue
    if n % 3 == 0:
        print("hop")
        continue
    if n % 5 == 0:
        print("hip")
        continue
    print(n)