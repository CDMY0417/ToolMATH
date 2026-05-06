def weighted_average(a: float, b: float, weight_a: float, weight_b: float):
    total_weight = weight_a + weight_b
    return (a * weight_a + b * weight_b) / total_weight
