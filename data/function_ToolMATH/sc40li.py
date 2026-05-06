def distribute_polynomials(poly1: list[float], poly2: list[float]) -> list[float]:
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, coef1 in enumerate(poly1):
        for j, coef2 in enumerate(poly2):
            result[i + j] += coef1 * coef2
    return result
