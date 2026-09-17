def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result

a = int(input("number: "))
b = int(input("time: "))

print(f"{a} ** {b} = {power(a, b)}")