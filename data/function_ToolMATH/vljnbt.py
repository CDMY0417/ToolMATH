def greatest_common_divisor_p(a_factors: dict[int, int], b_factors: dict[int, int]) -> int:
    gcd = 1
    common_primes = set(a_factors.keys()).intersection(set(b_factors.keys()))
    for prime in common_primes:
        gcd *= prime ** min(a_factors[prime], b_factors[prime])
    return gcd
