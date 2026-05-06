def find_polynomial_roots(coefficients: list[float]):
    import numpy as np
    poly = np.poly1d(coefficients)
    roots = poly.r
    return roots
