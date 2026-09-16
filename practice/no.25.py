numbers = [12, 7, 25, 40, 33, 18, 9, 6]
new_list = []

for number in numbers:
    if number % 2 == 0:
        new_list.append(number)

new_list.sort()
print(new_list)