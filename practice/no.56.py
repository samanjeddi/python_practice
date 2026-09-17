def is_even(n):
    return n % 2 == 0

def any_even_in_list(nums):
    count = 0
    for num in nums:
        if is_even(num):
            count += 1
    if count >= 1:
        return True
    else:
        return False

a = [1, 1, 3, 1, 5, 1, 7, 1, 9]
print(any_even_in_list(a))