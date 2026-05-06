def subtract_polynomials(poly1: tuple, poly2: tuple) -> tuple:
    max_len = max(len(poly1), len(poly2))
    poly1 = (0,) * (max_len - len(poly1)) + poly1
    poly2 = (0,) * (max_len - len(poly2)) + poly2
    return tuple(a - b for a, b in zip(poly1, poly2))
