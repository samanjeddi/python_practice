n = int(input("give me a number: "))
if n % 3 == 0 and n % 5 == 0:
    print("legend...")
elif n % 3 == 0:
    print("magic!..")
elif n % 5 == 0:
    print("cursed!!!")
else:
    print("normal!")