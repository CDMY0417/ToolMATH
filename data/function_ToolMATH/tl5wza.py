def common_prime_factors_a(factorization_a: dict[int, int], factorization_b: dict[int, int]) -> dict[int, int]:
    common_factors = {}
    for prime in factorization_a:
        if prime in factorization_b:
            common_factors[prime] = min(factorization_a[prime], factorization_b[prime])
    return common_factors
