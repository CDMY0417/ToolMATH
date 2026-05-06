def find_c_for_polynomial_identity(p: float, q: float, r: float, s: float, t: float):
    # Solve c so (x^2+px+q)(x+r) - (x^2+sx+t)(x-c) = 0 for all x
    # Compare coefficients of x^2: (p+r) - (s-c) = 0 -> c = s - p - r
    return s - p - r
