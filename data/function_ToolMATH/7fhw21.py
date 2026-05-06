def is_power_of_two_b(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
