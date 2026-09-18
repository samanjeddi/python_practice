def double_4(x):
    return x * 2 == 4

numbers = [1, 2, 3, 4, 5]
num = filter(double_4, numbers)

print(list(num))