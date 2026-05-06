def multiply_factors_a(factors: list[int]) -> int:
    result = 1
    for factor in factors:
        result *= factor
    return result
