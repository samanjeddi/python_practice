secret = 37
number = int(input("number: "))

while number != secret:
    if number > secret:
        print("too high...")
    elif number < secret:
        print("too low...")
    
    number = int(input("try again: "))

print("correct")