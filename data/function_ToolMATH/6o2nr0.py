def solve_linear_system_o(coefficients: list[list[float]], constants: list[float]):
    from sympy import symbols, Eq, solve
    t, s, u = symbols('t s u')
    eq1 = Eq(coefficients[0][0] * t + coefficients[0][1] * s + coefficients[0][2] * u, constants[0])
    eq2 = Eq(coefficients[1][0] * t + coefficients[1][1] * s + coefficients[1][2] * u, constants[1])
    eq3 = Eq(coefficients[2][0] * t + coefficients[2][1] * s + coefficients[2][2] * u, constants[2])
    solution = solve((eq1, eq2, eq3), (t, s, u))
    return solution
