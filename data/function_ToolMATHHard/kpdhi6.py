import math

def min_of_x2_linear_plus_inverse_power(b: float, c: float):
    """Return minimum value for x>0."""
    # f(x)=x^2 + b x + c/x^3. Set derivative: 2x + b - 3c/x^4 = 0
    # Solve 2x^5 + b x^4 - 3c = 0 numerically.
    import numpy as np
    coeffs = [2.0, b, 0.0, 0.0, 0.0, -3.0*c]
    roots = np.roots(coeffs)
    candidates = []
    for r in roots:
        if abs(r.imag) < 1e-8 and r.real > 0:
            x = r.real
            val = x*x + b*x + c/(x**3)
            candidates.append(val)
    if not candidates:
        raise ValueError("No positive critical point.")
    return min(candidates)
