def greatest_common_factor_j(num1: int, num2: int) -> int:
    def prime_factorization(n: int):
        factors = {}
        d = 2
        while n >= 2:
            while n % d == 0:
                if d in factors:
                    factors[d] += 1
                else:
                    factors[d] = 1
                n //= d
            d += 1
        return factors
    factors_a = prime_factorization(num1)
    factors_b = prime_factorization(num2)
    common_factors = set(factors_a.keys()).intersection(set(factors_b.keys()))
    gcf = 1
    for factor in common_factors:
        gcf *= factor ** min(factors_a[factor], factors_b[factor])
    return gcf
