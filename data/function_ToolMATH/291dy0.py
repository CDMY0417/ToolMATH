def solve_quadratic_eq(a: float, b: float, c: float):
    d = (b**2) - (4*a*c)
    sol1 = (-b + d**0.5) / (2*a)
    sol2 = (-b - d**0.5) / (2*a)
    return sol1, sol2
