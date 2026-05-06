def apply_percent_loss(initial_value: float, percent_loss: float) -> float:
    return initial_value * (1 - percent_loss / 100)
