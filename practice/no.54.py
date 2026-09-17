def number_of_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number_of_evens(a))