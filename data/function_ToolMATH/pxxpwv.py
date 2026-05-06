def solve_quadratic_inequality_b(a: int, b: int, c: int):
    from sympy import symbols, solve
    x = symbols('x')
    inequality = a * x**2 + b * x + c <= 0
    return solve(inequality, x)
