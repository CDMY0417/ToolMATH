def arctan_sum(x: float, y: float) -> float:
    numerator = x + y
    denominator = 1 - x * y
    return numerator / denominator
