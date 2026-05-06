def expand_polynomial_product(poly1: list[float], poly2: list[float]) -> list[float]:
    deg1 = len(poly1) - 1
    deg2 = len(poly2) - 1
    result = [0] * (deg1 + deg2 + 1)
    for i in range(deg1 + 1):
        for j in range(deg2 + 1):
            result[i + j] += poly1[i] * poly2[j]
    return result
