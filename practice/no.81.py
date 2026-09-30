def calculator(a, b, what_to_do):
    def add(a, b):
        return a + b
    def minus(a, b):
        return a - b
    def time(a, b):
        return a * b
    def divide(a, b):
        return a // b

    if what_to_do == 'add':
        return add(a, b)
    if what_to_do == 'minus':
        return minus(a, b)
    if what_to_do == 'time':
        return time(a, b)
    if what_to_do == 'divide':
        return divide(a, b)

a = int(input("first number: "))
b = int(input("second number: "))
what_to_do = input("what to do? ")

print(calculator(a, b, what_to_do))