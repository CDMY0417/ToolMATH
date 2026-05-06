def polynomial_multiplication(poly1: list[float], poly2: list[float]) -> list[float]:
    deg1 = len(poly1)
    deg2 = len(poly2)
    result = [0] * (deg1 + deg2 - 1)
    for i in range(deg1):
        for j in range(deg2):
            result[i + j] += poly1[i] * poly2[j]
    return result
