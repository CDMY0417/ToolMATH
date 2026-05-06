def logarithm_bounds(x: float, base: int):
    import math
    lower_bound = math.floor(math.log(x, base))
    upper_bound = lower_bound + 1
    return lower_bound, upper_bound
