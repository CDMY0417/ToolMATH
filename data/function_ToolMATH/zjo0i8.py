def is_integer_power_of_sqrt2(k: int) -> bool:
    import math
    if k <= 0:
        return False
    log_val = math.log(k, math.sqrt(2))
    return log_val.is_integer()
