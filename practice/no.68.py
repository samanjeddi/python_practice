def  pick_evens(*args):
    evens = []
    odds = []
    for a in args:
        if a % 2 == 0:
            evens.append(a)
        else:
            odds.append(a)
    return evens, odds

nums = pick_evens(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"evens are: {nums[0]}, odds are: {nums[1]}")