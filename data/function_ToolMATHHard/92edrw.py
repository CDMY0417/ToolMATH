def x_plus_reciprocal_from_quadratic(a: float, b: float, c: float):
    # For ax^2 + b x + c = 0, if c == a then x + 1/x = -b/a
    if abs(c - a) > 1e-12:
        raise ValueError('c must equal a to compute x + 1/x directly')
    return -b / a
