def rectangular_to_cylindrical_theta_a(x: float, y: float) -> float:
    from math import atan2, pi
    theta = atan2(y, x)
    return theta if theta >= 0 else theta + 2 * pi
