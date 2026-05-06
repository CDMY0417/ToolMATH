def value_at_position(initial_value: float, common_ratio: float, position: int):
    return initial_value * common_ratio ** (position - 1)
