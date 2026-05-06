def normalize_angle_e(theta: float) -> float:
    from math import pi
    while theta < 0:
        theta += 2 * pi
    while theta >= 2 * pi:
        theta -= 2 * pi
    return theta
