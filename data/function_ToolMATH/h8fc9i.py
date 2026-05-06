def solve_linear_system_3x3(coefficients: list[list[float]], constants: list[float]):
    from sympy import symbols, Eq, solve
    x, y, z = symbols('x y z')
    eq1 = Eq(coefficients[0][0] * x + coefficients[0][1] * y + coefficients[0][2] * z, constants[0])
    eq2 = Eq(coefficients[1][0] * x + coefficients[1][1] * y + coefficients[1][2] * z, constants[1])
    eq3 = Eq(coefficients[2][0] * x + coefficients[2][1] * y + coefficients[2][2] * z, constants[2])
    solution = solve((eq1, eq2, eq3), (x, y, z))
    return solution
