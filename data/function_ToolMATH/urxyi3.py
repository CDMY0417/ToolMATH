def compute_log_expression_value(coefficients: list[float], log_values: list[float]) -> float:
    return sum(c * lv for c, lv in zip(coefficients, log_values))
