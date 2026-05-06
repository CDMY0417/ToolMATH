def initial_quantity(final_value: float, reduction_factor: float, days: int):
    return final_value / (reduction_factor ** days)
