def evaluate_expression_e(expression: str, values: dict):
    from sympy import sympify
    expr = sympify(expression)
    return expr.evalf(subs=values)
