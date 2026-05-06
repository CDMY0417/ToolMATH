def add_polynomials_c(poly1: list[float], poly2: list[float]) -> list[float]:
    length = max(len(poly1), len(poly2))
    poly1 = poly1 + [0] * (length - len(poly1))
    poly2 = poly2 + [0] * (length - len(poly2))
    return [poly1[i] + poly2[i] for i in range(length)]
