text = input("write a line: ")

count = {
    "characters" : 0,
    "nums" : 0
}

for char in text:

    if char.isalpha():
        count["characters"] += 1

    elif char.isdigit():
        count["nums"] += 1

print(count)