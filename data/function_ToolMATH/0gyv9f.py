def gcd_using_factors(factors_a: dict, factors_b: dict) -> int:
    common_factors = set(factors_a.keys()).intersection(factors_b.keys())
    gcd = 1
    for factor in common_factors:
        gcd *= factor ** min(factors_a[factor], factors_b[factor])
    return gcd
