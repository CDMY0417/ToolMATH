def subtract_polynomials_c(poly1: list[float], poly2: list[float]) -> list[float]:
    length = max(len(poly1), len(poly2))
    result = [0] * length
    for i in range(length):
        coeff1 = poly1[i] if i < len(poly1) else 0
        coeff2 = poly2[i] if i < len(poly2) else 0
        result[i] = coeff1 - coeff2
    return result
