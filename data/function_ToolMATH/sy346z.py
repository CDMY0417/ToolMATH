def greatest_common_factor_n(factorization_a: dict[int, int], factorization_b: dict[int, int]) -> int:
    gcf = 1
    for p in factorization_a:
        if p in factorization_b:
            gcf *= p ** min(factorization_a[p], factorization_b[p])
    return gcf
