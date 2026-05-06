def solve_quadratic_be(a: float, b: float, c: float):
    import cmath
    d = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(d)) / (2*a)
    root2 = (-b - cmath.sqrt(d)) / (2*a)
    return root1, root2
