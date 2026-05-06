def compute_log_expression_x(x: float) -> float:
    from math import log, sqrt
    return log(x + sqrt(1 + x**2))
