def is_power_of_two(x: int) -> bool:
    from math import log2
    return log2(x).is_integer()
