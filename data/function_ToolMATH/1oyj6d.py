def tan_triple_angle(tan_theta: float) -> float:
    numerator = 3 * tan_theta - tan_theta**3
    denominator = 1 - 3 * tan_theta**2
    return numerator / denominator
