def weighted_sum_e(values: list, weights: list) -> int:
    return sum(value * weight for value, weight in zip(values, weights))
