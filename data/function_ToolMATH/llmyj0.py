def subtract_polynomials_b(poly1: dict[int, float], poly2: dict[int, float]) -> dict[int, float]:
    result = {}
    all_degrees = set(poly1.keys()).union(set(poly2.keys()))
    for degree in all_degrees:
        result[degree] = poly1.get(degree, 0) - poly2.get(degree, 0)
    return result
