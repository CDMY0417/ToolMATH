def solve_linear_equation_gb(a: int, b: int, c: int, d: int) -> float:
    from sympy import symbols, Eq, solve
    x = symbols('x')
    equation = Eq(a * x + b, c * x + d)
    solution = solve(equation, x)
    return solution[0]
