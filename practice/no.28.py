scores = {
    'ali' : 18,
    'reza' : 15,
    'sara' : 20,
    'mina' : 17,
}

highest_score = 0
highest_student = ""

for name in scores:
    if scores[name] > highest_score:
        highest_score = scores[name]
        highest_student = name

print(highest_student)
