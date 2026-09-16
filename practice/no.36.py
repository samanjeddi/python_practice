set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
result = set()

for set in set1:
    if set not in set2:
        result.add(set)

for set in set2:
    if set not in set1:
        result.add(set)

print(result)