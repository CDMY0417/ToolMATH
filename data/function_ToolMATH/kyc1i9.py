def solve_equation_system(eq1: tuple[float, float, float], eq2: tuple[float, float, float]):
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    equation1 = Eq(eq1[0] * x + eq1[1] * y, eq1[2])
    equation2 = Eq(eq2[0] * x + eq2[1] * y, eq2[2])
    return solve((equation1, equation2), (x, y))
