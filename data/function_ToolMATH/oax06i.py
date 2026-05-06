def max_multiple_with_remainder_less_than(m: int, r: int, limit: int) -> int:
    k = (limit - r) // m
    return m * k + r
