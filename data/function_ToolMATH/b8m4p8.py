def probability_product_c(probabilities: list[float]) -> float:
    product = 1.0
    for p in probabilities:
        product *= p
    return product
