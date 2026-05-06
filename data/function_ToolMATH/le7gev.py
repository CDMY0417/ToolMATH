def compare_coefficients(poly1: list[float], poly2: list[float]) -> list[float]:
    return [a - b for a, b in zip(poly1, poly2)]
