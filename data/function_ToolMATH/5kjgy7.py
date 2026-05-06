def count_factors_with_min_exponents(prime_factors: dict, min_exponents: dict) -> int:
    count = 1
    for prime, exp in prime_factors.items():
        min_exp = min_exponents.get(prime, 0)
        if exp >= min_exp:
            count *= (exp - min_exp + 1)
        else:
            return 0
    return count
