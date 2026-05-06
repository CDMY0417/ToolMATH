def gcd_from_factorizations(factors_a: dict[int, int], factors_b: dict[int, int]) -> int:
    gcd = 1
    for prime in factors_a:
        if prime in factors_b:
            gcd *= prime ** min(factors_a[prime], factors_b[prime])
    return gcd
