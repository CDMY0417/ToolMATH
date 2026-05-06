def log_base_change_a(value: int, base_a: int, base_b: int):
    import math
    return math.log(value, base_b) / math.log(base_a, base_b)
