def multipled_by(a, b):
    return(a * b)

def plus(a, b):
    return(a + b)

def minus(a, b):
    return(a - b)

def divided_by(a, b):
    return(a // b)

def tavan(a, b):
    return(a ** b)

first_num = int(input("first num: "))
second_num = int(input("second num: "))
between = input("write x , + , - , % , **: ")

if between == "x":
    print(f"{first_num} x {second_num} = {multipled_by(first_num, second_num)}")
elif between == "+":
    print(f"{first_num} + {second_num} = {plus(first_num, second_num)}")
elif between == "-":
    print(f"{first_num} - {second_num} = {minus(first_num, second_num)}")
elif between == "%":
    print(f"{first_num} % {second_num} = {divided_by(first_num, second_num)}")
elif between == "**":
    print(f"{first_num} ** {second_num} = {tavan(first_num, second_num)}")
