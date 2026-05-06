def largest_integer_less_than_with_remainder(limit: int, divisor: int, remainder: int) -> int:
    max_n = (limit - remainder) // divisor
    return divisor * max_n + remainder
