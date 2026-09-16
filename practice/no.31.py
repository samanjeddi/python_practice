students = {
    'ali' : 12,
    'reza' : 8,
    'sara' : 19,
    'mina' : 10,
    'amir' : 7,
}
passed_students = []

for student in students:
    if students[student] >= 10:
        passed_students.append(student)

print(passed_students)