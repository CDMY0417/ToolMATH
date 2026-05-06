def line_from_point_normal(a: float, b: float, x0: float, y0: float):
    """Return (m,b) for line with normal (a,b) through (x0,y0)."""
    # a(x-x0)+b(y-y0)=0 => y = (-a/b)x + (a*x0+b*y0)/b
    if b == 0:
        raise ValueError("b must be nonzero.")
    m = -a / b
    intercept = (a*x0 + b*y0) / b
    return [m, intercept]
