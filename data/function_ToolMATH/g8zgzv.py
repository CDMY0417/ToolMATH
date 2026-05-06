def find_intersection(m1: float, c1: float, m2: float, c2: float) -> tuple:
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return (x, y)
