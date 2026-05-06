def find_logarithm_bounds(x: int):
    import math
    lower_bound = int(math.log10(x))
    upper_bound = lower_bound + 1
    return lower_bound, upper_bound
