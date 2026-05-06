def intersection_of_lines_b(m1: float, c1: float, m2: float, c2: float):
    if m1 == m2:
        return None # Parallel lines
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return (x, y)
