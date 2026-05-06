def calculate_theta(x: float, y: float) -> float:
    import math
    if x == 0 and y == 0:
        return 0
    return math.atan2(y, x)
