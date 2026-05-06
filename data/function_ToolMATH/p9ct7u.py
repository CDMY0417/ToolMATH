def count_multiples_in_range_n(start: int, end: int, divisor: int) -> int:
    first = (start + divisor - 1) // divisor
    last = end // divisor
    return last - first + 1
