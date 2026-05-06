def find_line_intersection(m1: float, b1: float, m2: float, b2: float) -> tuple:
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)
