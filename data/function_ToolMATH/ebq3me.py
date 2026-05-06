def greatest_common_divisor_from_factors(factors_a: list[int], factors_b: list[int]) -> int:
    common_factors = []
    for factor in set(factors_a).intersection(factors_b):
        common_factors.extend([factor] * min(factors_a.count(factor), factors_b.count(factor)))
    gcd = 1
    for factor in common_factors:
        gcd *= factor
    return gcd
