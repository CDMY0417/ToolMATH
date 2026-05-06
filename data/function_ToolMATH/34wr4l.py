def simplify_equation(equation: str) -> str:
    import sympy as sp
    left_side, right_side = equation.split('=')
    expr = sp.sympify(left_side)
    simplified_expr = sp.simplify(expr)
    return str(simplified_expr) + '=' + right_side
