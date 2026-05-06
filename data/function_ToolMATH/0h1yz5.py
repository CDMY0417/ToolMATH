def solve_quad_by_factoring(a: int, b: int, c: int):
    import sympy as sp
    x = sp.symbols('x')
    equation = a*x**2 + b*x + c
    roots = sp.solve(equation, x)
    return roots
