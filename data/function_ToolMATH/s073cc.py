def solve_for_variable_g(equations: tuple, variable: str):
    from sympy import solve
    solution = solve(equations, variable)
    return solution[0]
