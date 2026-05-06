def factor_quadratic_m(a: int, b: int, c: int):
    import sympy as sp
    x = sp.symbols('x')
    expr = a * x**2 + b * x + c
    factors = sp.factor(expr)
    return factors.args if factors.is_Mul else (factors,)
