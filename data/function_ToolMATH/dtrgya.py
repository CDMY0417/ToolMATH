def subtract_polynomials_d(poly1: list[float], poly2: list[float]) -> list[float]:
    max_len = max(len(poly1), len(poly2))
    # Extend both polynomials to the max length with zeros
    poly1.extend([0] * (max_len - len(poly1)))
    poly2.extend([0] * (max_len - len(poly2)))
    return [coeff1 - coeff2 for coeff1, coeff2 in zip(poly1, poly2)]
