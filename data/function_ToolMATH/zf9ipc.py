def simplify_expression_c(expression: str, power: int):
    from sympy import symbols, simplify
    x = symbols('x')
    simplified_expr = simplify(expression)
    return simplified_expr.coeff(x**power)
