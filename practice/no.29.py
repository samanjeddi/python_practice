text = 'programming'
count = {}

for t in text:
    if t in count:
        count[t] += 1
    else:
        count[t] = 1

print(count)