def largest_power_of_factor_in_factorial(n: int, p: int) -> int:
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count
