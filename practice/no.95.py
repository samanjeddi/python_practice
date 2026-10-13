from random import randint

def odd_or_even():
    num = randint(1, 100)
    print(num)

    if num % 2 == 0:
        print("even number")
    elif num % 2 != 0:
        print("odd number")

odd_or_even()