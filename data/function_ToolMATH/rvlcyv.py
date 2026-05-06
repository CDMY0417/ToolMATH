def gcd_from_factors(factors_a: dict[int, int], factors_b: dict[int, int]) -> int:
    gcd = 1
    for p in factors_a:
        if p in factors_b:
            gcd *= p ** min(factors_a[p], factors_b[p])
    return gcd
