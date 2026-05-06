def solve_quadratic_equation_v(a: int, b: int, c: int):
    D = b**2 - 4*a*c
    if D < 0:
        return []
    elif D == 0:
        return [-b / (2*a)]
    else:
        root1 = (-b + D**0.5) / (2*a)
        root2 = (-b - D**0.5) / (2*a)
        return [root1, root2]
