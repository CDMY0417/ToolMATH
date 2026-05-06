def distance_squared_on_unit_circle(theta1: float, theta2: float) -> float:
    import math
    return 2 * (1 - math.cos(theta1 - theta2))
