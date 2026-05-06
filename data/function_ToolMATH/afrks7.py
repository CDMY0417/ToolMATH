def product_of_factors_c(factors: list[float]) -> float:
    product = 1
    for factor in factors:
        product *= factor
    return product
