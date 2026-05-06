def polynomial_multiply(poly1: list[float], poly2: list[float]) -> list[float]:
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, coeff1 in enumerate(poly1):
        for j, coeff2 in enumerate(poly2):
            result[i + j] += coeff1 * coeff2
    return result
