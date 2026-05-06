def sum_cosine_angles(angle1: float, angle2: float) -> float:
    from math import cos
    return 2 * cos((angle1 + angle2) / 2) * cos((angle1 - angle2) / 2)
