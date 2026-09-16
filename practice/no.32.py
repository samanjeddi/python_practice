scores = {
    'ali' : 75,
    'reza' : 95,
    'sara' : 88,
    'mina' : 95,
    'amir' : 92,
}
largest = 0

for score in scores:
    if scores[score] > largest:
        largest = scores[score]

second = 0

for score in scores:
    if scores[score] < largest:
        if scores[score] > second:
             second = scores[score]

print(second)