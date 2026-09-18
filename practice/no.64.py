def is_greater(a, b):
    if a > b:
        return True
    if a < b:
        return False
    return "equal"

num1 = int(input("first number: "))
num2 = int(input("second number: "))

print(is_greater(num1, num2))