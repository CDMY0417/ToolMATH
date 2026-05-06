def line_intersection_a(m1: float, c1: float, m2: float, c2: float):
    if m1 == m2:
        return None  # Lines are parallel and do not intersect
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return (x, y)
