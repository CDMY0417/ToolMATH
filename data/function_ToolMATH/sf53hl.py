def factor_polynomial_b(expression: str):
    # This function uses sympy to factor polynomials
    from sympy import sympify, factor
    expr = sympify(expression)
    return factor(expr)
