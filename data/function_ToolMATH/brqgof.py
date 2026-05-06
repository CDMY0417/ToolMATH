def smallest_number_with_factors(factors: set[int]) -> int:
    product = 1
    for factor in factors:
        product *= factor
    return product
