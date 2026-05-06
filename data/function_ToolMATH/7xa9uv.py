def count_multiples_in_range_b(start: int, end: int, divisor: int) -> int:
    first_multiple = (start + divisor - 1) // divisor
    last_multiple = end // divisor
    return last_multiple - first_multiple + 1
