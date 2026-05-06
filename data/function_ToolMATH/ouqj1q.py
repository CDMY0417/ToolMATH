def next_multiple_a(start: int, divisor: int) -> int:
    remainder = start % divisor
    if remainder == 0:
        return start
    return start + divisor - remainder
