def find_largest(n):
    n.sort()
    return n[-1]

a = [12, 45, 7, 89, 34]
print(find_largest(a))

# find largest number without using max