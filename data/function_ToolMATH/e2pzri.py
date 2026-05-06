def prime_factorization_cj(n: int):
    factors = {}
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            if factor in factors:
                factors[factor] += 1
            else:
                factors[factor] = 1
            n //= factor
        factor += 1
    if n > 1:
        factors[n] = 1
    return factors
