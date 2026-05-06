def solve_quartic(a: float, b: float, c: float, d: float, e: float):
    import numpy as np
    coefficients = [a, b, c, d, e]
    roots = np.roots(coefficients)
    return roots
