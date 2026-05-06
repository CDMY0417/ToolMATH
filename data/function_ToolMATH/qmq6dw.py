def apply_log_power_rule(coefficients: list[float], logs: list[float]) -> list[float]:
    result = []
    for coef, log_value in zip(coefficients, logs):
        result.append(coef * log_value)
    return result
