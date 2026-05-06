def calculate_angle_ratio(ratios: list[float], angle_sum: float):
    k = angle_sum / sum(ratios)
    return [ratio * k for ratio in ratios]
