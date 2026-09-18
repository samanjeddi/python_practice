def zarb(*args):
    result = 1
    for a in args:
        result *= a
    return result

num = zarb(1, 2, 3, 4, 5)
print(num)