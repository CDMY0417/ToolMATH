def prime_factorization_exponent(n: int, prime_factor: int) -> int:
    count = 0
    while n % prime_factor == 0:
        n //= prime_factor
        count += 1
    return count
