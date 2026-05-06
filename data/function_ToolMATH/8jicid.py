def rectangular_to_cylindrical_theta(x: int, y: int) -> float:
    import math
    if x == 0 and y == 0:
        return 0
    theta = math.atan2(y, x)
    if theta < 0:
        theta += 2 * math.pi
    return theta
