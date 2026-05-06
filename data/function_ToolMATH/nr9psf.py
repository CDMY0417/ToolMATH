def exponent_in_prime_factorization(n: int, prime: int) -> int:
    exponent = 0
    while n % prime == 0:
        n //= prime
        exponent += 1
    return exponent
