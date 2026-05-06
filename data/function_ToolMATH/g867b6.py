def factor_common_term(expression: str, common_factor: str):
    import sympy as sp
    expr = sp.sympify(expression)
    factor = sp.sympify(common_factor)
    factored_expr = sp.factor(expr)
    simplified_expr = factored_expr / factor
    return f'{factor}({simplified_expr})'
