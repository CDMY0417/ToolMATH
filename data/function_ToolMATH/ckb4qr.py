def compute_theta(x: float, y: float) -> float:
    import math
    return math.atan2(y, x) % (2 * math.pi)
