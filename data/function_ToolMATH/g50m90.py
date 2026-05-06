def count_factors_in_factorial_e(n: int, p: int) -> int:
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count
