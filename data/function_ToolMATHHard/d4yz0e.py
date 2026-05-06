import math

def solve_rational_equation_quadratic(a: float, b: float, c: float, d: float, k: float):
    """Return real solutions of the equation."""
    # Multiply by x(x-b): a x^2 + (c x^2 + d)(x-b) = k x(x-b)
    # Expand to quadratic
    # (c x^2 + d)(x-b) = c x^3 - b c x^2 + d x - b d
    # Equation: c x^3 + (a - b c) x^2 + d x - b d - k x^2 + k b x = 0
    # If c=0, becomes quadratic; here c=2.
    # Use numeric roots from polynomial
    coeff3 = c
    coeff2 = a - b*c - k
    coeff1 = d + k*b
    coeff0 = -b*d
    # solve cubic numerically, keep reals
    import numpy as np
    roots = np.roots([coeff3, coeff2, coeff1, coeff0])
    sols = []
    for r in roots:
        if abs(r.imag) < 1e-8:
            x = r.real
            if abs(x) < 1e-9 or abs(x - b) < 1e-9:
                continue
            sols.append(x)
    return sorted(sols)
