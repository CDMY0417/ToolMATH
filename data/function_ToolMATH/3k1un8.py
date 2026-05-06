def change_of_base(log_value: float, from_base: float, to_base: float) -> float:
    from math import log
    return log_value * (log(to_base) / log(from_base))
