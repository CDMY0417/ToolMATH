def change_of_base_logarithm_a(log_x_base_a: float, base_a: int, base_b: int) -> float:
    from math import log
    return log(base_b) * log_x_base_a / log(base_a)
