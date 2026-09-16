numbers = [10, 45, 23, 89, 67, 89, 34]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

second = None

for number in numbers:
    if number < largest:
        if second is None or number > second:
            second = number

print(second)