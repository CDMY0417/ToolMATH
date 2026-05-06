def count_multiples_in_range_r(start: int, end: int, divisor: int) -> int:
    return len([i for i in range(start, end + 1) if i % divisor == 0])
