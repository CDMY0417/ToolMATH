def largest_power_prime_factorial(n: int, p: int) -> int:
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count
