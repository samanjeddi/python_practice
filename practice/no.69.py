def skyline(*args):
    highest = 0
    for a in args:
        if a > highest:
            highest = a
    return highest

skylines_height = skyline(200, 300, 650, 720, 110)
print(skylines_height)