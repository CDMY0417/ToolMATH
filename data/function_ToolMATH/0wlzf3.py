def exponential_decay(initial_quantity: float, decay_factor: float, intervals: int) -> float:
    return initial_quantity * (decay_factor ** intervals)
