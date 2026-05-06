def probability_weighted_sum(values: list[float], probabilities: list[float]) -> float:
    expected_value = sum(v * p for v, p in zip(values, probabilities))
    return expected_value
