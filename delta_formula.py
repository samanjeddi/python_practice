a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
delta = (b ** 2) - (4 * a * c)
print("delta:", delta)
if delta > 0:
    javab_1 = ((-b) - (delta ** (1 / 2))) / (2 * a)
    javab_2 = ((-b) + (delta ** (1 / 2))) / (2 * a)
    print("javab_1:", javab_1)
    print("javab_2:", javab_2)
else:
    print("javab nadarad")