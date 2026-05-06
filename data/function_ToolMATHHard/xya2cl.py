def perpendicular_bisector_intersection(p1x,p1y,p2x,p2y,q1x,q1y,q2x,q2y):
    """Return intersection of perpendicular bisectors."""
    # Midpoints
    m1x = (p1x + p2x) / 2.0
    m1y = (p1y + p2y) / 2.0
    m2x = (q1x + q2x) / 2.0
    m2y = (q1y + q2y) / 2.0
    # Direction vectors of segments
    d1x = p2x - p1x
    d1y = p2y - p1y
    d2x = q2x - q1x
    d2y = q2y - q1y
    # Perpendicular bisector directions
    n1x, n1y = -d1y, d1x
    n2x, n2y = -d2y, d2x
    # Solve m1 + t*n1 = m2 + s*n2
    det = n1x * (-n2y) - n1y * (-n2x)
    if det == 0:
        raise ValueError("Bisectors are parallel.")
    dx = m2x - m1x
    dy = m2y - m1y
    t = (dx * (-n2y) - dy * (-n2x)) / det
    x = m1x + t * n1x
    y = m1y + t * n1y
    return [x, y]
