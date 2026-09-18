def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
num = map(double, numbers)

print(list(num))