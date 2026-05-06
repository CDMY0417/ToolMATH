def smallest_multiple_greater_than(n: int, threshold: int) -> int:
    quotient = threshold // n
    return n * (quotient + 1)
