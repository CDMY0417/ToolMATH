def product_of_factors_a(factors: list[int]) -> int:
    product = 1
    for factor in factors:
        product *= factor
    return product
