def intersection_of_lines_c(m1: float, b1: float, m2: float, b2: float):
    if m1 == m2:
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)
