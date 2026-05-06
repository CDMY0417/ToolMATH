def median_item_in_weighted_values(weights: list[int], values: list[int]) -> int:
    total_count = sum(weights)
    cumulative_count = 0
    for weight, value in zip(weights, values):
        cumulative_count += weight
        if cumulative_count > total_count / 2:
            return value
    return None
