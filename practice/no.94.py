import itertools as it

nums = [1, 2, 3, 4]

a = it.combinations(nums, 2)
print(list(a))

a = it.combinations_with_replacement(nums, 2)
print(list(a))

a = it.accumulate(nums)
print(list(a))