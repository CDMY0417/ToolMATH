def change_of_base_log(log_base: float, log_value: float) -> float:
    from math import log
    return log(log_value) / log(log_base)
