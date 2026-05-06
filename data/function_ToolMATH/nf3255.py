def arctan_to_sin_cos(x: float):
    import math
    cos_theta = 1 / math.sqrt(x**2 + 1)
    sin_theta = x / math.sqrt(x**2 + 1)
    return sin_theta, cos_theta
