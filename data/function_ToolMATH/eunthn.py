def solve_quadratic_transformed(a: int, c: int):
    from math import sqrt
    x1 = a + sqrt(c)
    x2 = a - sqrt(c)
    return x1, x2
