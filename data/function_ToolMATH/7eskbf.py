def substitute_and_simplify(expression: str, substitutions: dict):
    from sympy import symbols, simplify
    expr = simplify(expression.format(**substitutions))
    return expr
