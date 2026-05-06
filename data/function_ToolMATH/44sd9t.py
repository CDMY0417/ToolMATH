def calculate_weight_loss(initial_weight: float, percentage_loss: float, weeks: int) -> float:
    final_weight = initial_weight * ((1 - percentage_loss) ** weeks)
    return final_weight
