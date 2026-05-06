def rect_to_polar_angle(x: float, y: float) -> float:
    import math
    theta = math.atan2(y, x)
    if theta < 0:
        theta += 2 * math.pi
    return theta
