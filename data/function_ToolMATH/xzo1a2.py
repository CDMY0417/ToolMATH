def prime_factorization_exponents_a(n: int):
    from collections import defaultdict
    factor_exponents = defaultdict(int)
    factor = 2
    while n % factor == 0:
        factor_exponents[factor] += 1
        n //= factor
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factor_exponents[factor] += 1
            n //= factor
        factor += 2
    if n > 1:
        factor_exponents[n] += 1
    return dict(factor_exponents)
