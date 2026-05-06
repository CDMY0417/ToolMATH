def substitute_value_a(expression: str, value_dict: dict):
    import sympy as sp
    expr = sp.sympify(expression)
    result = expr.subs(value_dict)
    return result.evalf()
