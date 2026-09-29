def divis(a, b):
    try:
        return a//b
    except ZeroDivisionError:
        print("you can't divide a number with zero")
    except Exception as e:
        print(f"another Error: {e}")

num1 = int(input("first number: "))
num2 = int(input("second number: "))

print(divis(num1, num2))