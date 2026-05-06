def product_of_factors_b(factors: dict[int, int]) -> int:
    result = 1
    for base, exponent in factors.items():
        result *= base ** exponent
    return result
