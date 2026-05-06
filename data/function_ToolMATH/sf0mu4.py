def gcd_using_prime_factors(factors1: dict[int, int], factors2: dict[int, int]) -> int:
    common_factors = {}
    for factor in factors1:
        if factor in factors2:
            common_factors[factor] = min(factors1[factor], factors2[factor])
    gcd = 1
    for factor, exponent in common_factors.items():
        gcd *= factor ** exponent
    return gcd
