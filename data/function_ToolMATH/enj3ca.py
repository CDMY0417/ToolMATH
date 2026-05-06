def prime_factorization_ci(n: int):
    factors = []
    d = 2
    while n >= d * d:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors
