def count_divisible_in_range(min_val: int, max_val: int, divisor: int):
    start = (min_val + divisor - 1) // divisor
    end = max_val // divisor
    return end - start + 1
