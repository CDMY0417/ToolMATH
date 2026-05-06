def magnitude_of_product(magnitudes: list[float]) -> float:
    product = 1
    for magnitude in magnitudes:
        product *= magnitude
    return product
