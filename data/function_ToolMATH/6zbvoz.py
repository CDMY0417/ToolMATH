def prime_factorization_s(n: int):
    factors = []
    if n <= 1:
        return factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    if n > 2:
        factors.append(n)
    return factors
