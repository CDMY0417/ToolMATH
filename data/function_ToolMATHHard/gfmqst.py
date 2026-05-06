def closest_point_on_line(m: float, b: float, x0: float, y0: float):
    """Return closest point on line y=mx+b."""
    # projection onto line
    # line in ax+by+c=0 with a=m, b=-1, c=b
    a = m
    bb = -1.0
    c = b
    denom = a*a + bb*bb
    t = (a*x0 + bb*y0 + c) / denom
    x = x0 - a*t
    y = y0 - bb*t
    return [x, y]
