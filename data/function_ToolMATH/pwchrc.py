def largest_multiple_less_than_d(n: int, limit: int) -> int:
    k = (limit - 1) // n
    return k * n
