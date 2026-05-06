def subtract_polynomials_h(poly1: list[float], poly2: list[float]) -> list[float]:
    return [a - b for a, b in zip(poly1, poly2)] + poly1[len(poly2):] + [-b for b in poly2[len(poly1):]]
