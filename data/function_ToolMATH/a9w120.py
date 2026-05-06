def tangent_sum_angle(a: float, b: float) -> float:
    from math import sin, cos
    return (sin(a) * cos(b) + cos(a) * sin(b)) / (cos(a) * cos(b))
