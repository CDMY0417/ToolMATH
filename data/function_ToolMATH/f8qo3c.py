def weighted_mean(mean1: float, weight1: int, mean2: float, weight2: int):
    total_weight = weight1 + weight2
    weighted_mean = (mean1 * weight1 + mean2 * weight2) / total_weight
    return weighted_mean
