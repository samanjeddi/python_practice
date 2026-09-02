from random import randint
a = randint(1, 6)
i = int(input('guess a number: '))
if i == a:
    print("Wow....")
else:
    print(f"no it was, {a}")
