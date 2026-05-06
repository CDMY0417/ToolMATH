def rectangular_to_spherical_theta(x: float, y: float) -> float:
    from math import atan2
    return atan2(y, x)
