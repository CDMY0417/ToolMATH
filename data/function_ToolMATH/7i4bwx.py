def solve_linear_equation_af(equation: str, variable: str):
    import sympy as sp
    lhs, rhs = equation.split('=')
    lhs, rhs = sp.sympify(lhs), sp.sympify(rhs)
    solution = sp.solve(lhs - rhs, variable)
    return solution[0]
