def remaining_after_halving(initial_value: int, num_halvings: int) -> int:
    return initial_value * (0.5 ** num_halvings)
