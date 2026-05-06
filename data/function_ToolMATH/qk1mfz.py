def count_factors_in_factorial_c(n: int, p: int) -> int:
    count = 0
    power = p
    while n >= power:
        count += n // power
        power *= p
    return count
