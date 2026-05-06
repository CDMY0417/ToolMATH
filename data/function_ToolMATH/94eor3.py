def solve_quadratic_equation_g(a: float, b: float, c: float) -> tuple:
    import cmath
    d = cmath.sqrt(b**2 - 4*a*c)
    sol1 = (-b + d) / (2*a)
    sol2 = (-b - d) / (2*a)
    return (sol1, sol2)
