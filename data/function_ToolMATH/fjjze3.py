def compute_square_root_from_factors(factors: dict[int, int]) -> int:
    product = 1
    for prime, exponent in factors.items():
        product *= prime ** (exponent // 2)
    return product
