def count_valid_years(lower_bound: int, upper_bound: int, divisor: int, addend: int) -> int:
    count = 0
    start = lower_bound - (lower_bound % divisor) + addend
    if start < lower_bound:
        start += divisor
    while start < upper_bound:
        count += 1
        start += divisor
    return count
