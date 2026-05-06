def sin_sum_of_angles(alpha: float, beta: float) -> float:
    from math import sin, cos, radians
    return sin(radians(alpha)) * cos(radians(beta)) + cos(radians(alpha)) * sin(radians(beta))
