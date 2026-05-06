def factorial_prime_exponent(n: int, prime: int):
    count = 0
    power = prime
    while power <= n:
        count += n // power
        power *= prime
    return count
