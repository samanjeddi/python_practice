num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))

if num1 == num2 and num2 == num3:
    print("three numbers are equal.")

elif (num1 == num2) or (num2 == num3) or (num1 == num3):
    print("two numbers are equal.")

else:
    print("no numbers are equal")