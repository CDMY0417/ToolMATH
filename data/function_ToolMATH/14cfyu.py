def count_distinct_digit_numbers(base: int, num_digits: int) -> int:
    if num_digits == 1:
        return base - 1
    count = (base - 1)
    for i in range(1, num_digits):
        count *= (base - 1 - i)
    return count
