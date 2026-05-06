def calculate_ratio_components(ratios: list[float], total_sum: float) -> list[float]:
    ratio_sum = sum(ratios)
    x = total_sum / ratio_sum
    return [r * x for r in ratios]
