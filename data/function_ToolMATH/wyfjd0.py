def is_sum_of_squares_greater(nums: tuple):
    a, b, c = sorted(nums)
    return a**2 + b**2 > c**2
