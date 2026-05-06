def find_interval(value: float) -> tuple:
    import math
    lower = math.floor(value)
    upper = math.ceil(value)
    return lower, upper
