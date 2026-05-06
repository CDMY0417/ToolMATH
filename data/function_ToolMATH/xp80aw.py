def solve_quadratic_equation_av(a: int, b: int, c: int):
    from sympy import symbols, solve
    x = symbols('x')
    equation = a*x**2 + b*x + c
    return solve(equation, x)
