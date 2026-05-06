def factorial_prime_factor_count(n: int, prime: int) -> int:
    count = 0
    power = prime
    while power <= n:
        count += n // power
        power *= prime
    return count
