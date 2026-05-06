def factor_quadratic_z(a: int, b: int, c: int):
    # Check if the quadratic is a perfect square trinomial
    if b**2 == 4 * a * c:
        root = -b // (2 * a)
        return (root, root)
    return None
