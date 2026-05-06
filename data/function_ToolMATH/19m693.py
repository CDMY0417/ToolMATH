def complete_square_a(a: int, b: int, c: int) -> tuple[float, float]:
    h = -b / (2 * a)
    k = c - (b**2) / (4 * a)
    return (h, k)
