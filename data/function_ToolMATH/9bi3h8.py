def sin_four_theta(sin_theta: float, cos_theta: float) -> float:
    sin_2theta = 2 * sin_theta * cos_theta
    cos_2theta = 2 * cos_theta**2 - 1
    sin_4theta = 2 * sin_2theta * cos_2theta
    return sin_4theta
