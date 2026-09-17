def count_positive(nums):
    positive_nums = []
    for num in nums:
        if num > 0:
            positive_nums.append(num)
    return positive_nums

a = [12, 34, 0, -4, 2]
print(f"in {a} , {count_positive(a)} are positive numbers.")