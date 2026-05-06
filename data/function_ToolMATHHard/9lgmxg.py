def sum_coordinates_intersections_parabolas(h: float, k: float, c: float, d: float):
    """Return sum of x and y coordinates of all intersections."""
    # Solve y = (x+h)^2 + k; x + c = (y - d)^2.
    # Substitute y; solve quartic numerically, then sum.
    import numpy as np
    # Coefficients for x from substitution:
    # x + c = ((x+h)^2 + k - d)^2
    # Expand: ((x+h)^2 + (k-d))^2 - x - c = 0
    # Let u = (x+h)^2 + (k-d)
    # Use numpy to expand
    import sympy as sp
    x=sp.symbols('x')
    expr = ((x+h)**2 + (k-d))**2 - x - c
    poly = sp.expand(expr)
    coeffs = [float(poly.expand().coeff(x,i)) for i in range(4,-1,-1)]
    roots = np.roots(coeffs)
    total = 0.0
    for r in roots:
        if abs(r.imag) < 1e-8:
            xr = r.real
            yr = (xr + h)**2 + k
            total += xr + yr
    return total
