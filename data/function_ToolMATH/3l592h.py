def cubic_polynomial_roots(a: float, b: float, c: float, d: float):
    import numpy as np
    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    return roots
