def solve_for_variable_d(equation: str, variable: str):
    import sympy as sp
    lhs, rhs = equation.split('=')
    eq = sp.Eq(sp.sympify(lhs), sp.sympify(rhs))
    solution = sp.solve(eq, variable)
    return solution
