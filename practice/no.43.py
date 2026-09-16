numbers = [2, 5, 2, 8, 5, 2, 9, 8, 5, 5]

most_common = None
max_count = 0

for number in numbers:
    count = 0

    for x in numbers:
        if x == number:
            count += 1

    if count > max_count:
        max_count = count
        most_common = number

print("number: ", most_common)
print("count: ", max_count)