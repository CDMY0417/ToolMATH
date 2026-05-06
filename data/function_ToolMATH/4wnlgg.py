def expected_value_a(values: list[float], weights: list[float]) -> float:
    total_weight = sum(weights)
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    return weighted_sum / total_weight
