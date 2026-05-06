def compute_roots_of_complex_number(r: float, theta: float, n: int):
    roots = []
    for k in range(n):
        angle = (theta + 360 * k) / n
        roots.append((r ** (1/n), angle))
    return roots
