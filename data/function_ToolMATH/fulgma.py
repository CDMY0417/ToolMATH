def solve_linear_system_k(equations: list[list[float]]) -> tuple:
    from sympy import symbols, Eq, solve
    a, b, c = symbols('a b c')
    eq1 = Eq(equations[0][0] * a + equations[0][1] * b + equations[0][2] * c, equations[0][3])
    eq2 = Eq(equations[1][0] * a + equations[1][1] * b + equations[1][2] * c, equations[1][3])
    eq3 = Eq(equations[2][0] * a + equations[2][1] * b + equations[2][2] * c, equations[2][3])
    solution = solve((eq1, eq2, eq3), (a, b, c))
    return solution[a], solution[b], solution[c]
