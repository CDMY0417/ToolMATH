def distribute_terms_and_simplify(expr: list):
    from sympy import simplify, expand
    expr_expanded = [expand(e) for e in expr]
    combined_expr = sum(expr_expanded)
    simplified_expr = simplify(combined_expr)
    return simplified_expr
