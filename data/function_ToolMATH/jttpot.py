def sum_sine_angles(angle1: float, angle2: float) -> float:
    from math import sin, cos
    return 2 * sin((angle1 + angle2) / 2) * cos((angle1 - angle2) / 2)
