def absolute_value_sum_piecewise(x: float, breakpoints: list[float]) -> float:
    result = 0
    for point in breakpoints:
        result += abs(x - point)
    return result
