def least_multiple_greater_than(base: int, number: int) -> int:
    quotient = number // base
    return base * (quotient + 1)
