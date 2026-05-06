def compute_slope_from_expression(y_expr: str) -> float:
    parts = y_expr.split('x')
    slope = float(parts[0].split()[-1])
    return slope
