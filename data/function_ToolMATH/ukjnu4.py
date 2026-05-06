def subtract_expressions(lhs: str, rhs: str):
    import sympy as sp
    lhs_expr = sp.sympify(lhs.replace('=', ''))
    rhs_expr = sp.sympify(rhs.replace('=', ''))
    diff = lhs_expr - rhs_expr
    return str(diff.simplify())
