def greatest_common_factor_d(factorization_a: dict[int, int], factorization_b: dict[int, int]) -> int:
    common_factors = {}
    for prime in factorization_a:
        if prime in factorization_b:
            common_factors[prime] = min(factorization_a[prime], factorization_b[prime])
    gcf = 1
    for prime, power in common_factors.items():
        gcf *= prime ** power
    return gcf
