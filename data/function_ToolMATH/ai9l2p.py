def factor_quadratic_ah(a: int, b: int, c: int):
    import sympy as sp
    x = sp.symbols('x')
    expr = a*x**2 + b*x + c
    factors = sp.factor(expr)
    return factors
