def prime_factorization_count(n: int, base: int) -> int:
    count = 0
    while n % base == 0:
        n //= base
        count += 1
    return count
