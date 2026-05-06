def count_factors_in_factorial_b(n: int, prime: int) -> int:
    count = 0
    power = prime
    while power <= n:
        count += n // power
        power *= prime
    return count
