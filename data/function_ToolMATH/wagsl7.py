def product_of_roots_by_vieta(coefficients: list[float]) -> float:
    n = len(coefficients) - 1
    return (-1)**n * coefficients[-1] / coefficients[0]
