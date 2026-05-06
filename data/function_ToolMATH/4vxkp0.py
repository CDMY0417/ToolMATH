def prime_factors_c(n: int) -> set:
    factors = set()
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            factors.add(factor)
            n //= factor
        factor += 1
    if n > 1:
        factors.add(n)
    return factors
