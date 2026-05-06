def prime_factors_x(n: int) -> dict:
    factors = {}
    d = 2
    while n >= d * d:
        while (n % d) == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors
