def solve_linear_system_l(coeff1_x: float, coeff1_y: float, rhs1: float, coeff2_x: float, coeff2_y: float, rhs2: float):
    from sympy import symbols, Eq, solve
    x, y = symbols('x y')
    eq1 = Eq(coeff1_x * x + coeff1_y * y, rhs1)
    eq2 = Eq(coeff2_x * x + coeff2_y * y, rhs2)
    solution = solve((eq1, eq2), (x, y))
    return solution[x], solution[y]
