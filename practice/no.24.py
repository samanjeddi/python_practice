numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
new_list = []

for number in numbers:
    if number not in new_list:
        new_list.append(number)

print(new_list)