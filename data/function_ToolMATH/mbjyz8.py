def monic_quadratic_from_roots_a(root1: float, root2: float):
    a = 1.0
    b = -(root1 + root2)
    c = root1 * root2
    return (a, b, c)
