def cubic_equation(a: int, b: int, c: int, d: int):
    import sympy as sp
    x = sp.symbols('x')
    eq = a*x**3 + b*x**2 + c*x + d
    solutions = sp.solve(eq, x)
    return solutions
