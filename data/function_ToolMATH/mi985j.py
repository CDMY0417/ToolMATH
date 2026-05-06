def factor_polynomial_a(poly: str):
    from sympy import factor, symbols
    x = symbols('x')
    return factor(poly)
