def exponent_in_prime_factorization_a(n: int, p: int) -> int:
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count
