def substitute_in_expression(expr: str, value: float) -> str:
    import sympy as sp
    y = sp.Symbol('y')
    expr = sp.sympify(expr)
    return str(expr.subs(y, value))
