def probability_product(fractions: list[float]) -> float:
    product = 1.0
    for fraction in fractions:
        product *= fraction
    return product
