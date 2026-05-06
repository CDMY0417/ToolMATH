def calculate_remaining_percentage(total: float, percentages: list[float]) -> float:
    remaining_percentage = total - sum(percentages)
    return remaining_percentage
