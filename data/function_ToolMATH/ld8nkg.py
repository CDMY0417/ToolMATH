def least_addition_for_multiple(n: int, m: int) -> int:
    remainder = n % m
    return m - remainder if remainder != 0 else 0
