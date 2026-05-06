def evaluate_polynomial_at_points(polynomial: str, points: list[float]) -> list[float]:
    from sympy import sympify, symbols
    x = symbols('x')
    poly_expr = sympify(polynomial)
    return [poly_expr.subs(x, pt) for pt in points]
