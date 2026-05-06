def integer_power_factorization(n: int):
    factors = {}
    factor = 2
    while n % factor == 0:
        factors[factor] = factors.get(factor, 0) + 1
        n //= factor
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors[factor] = factors.get(factor, 0) + 1
            n //= factor
        factor += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors
