def angle_difference_multiple_of_two_pi(angle1: float, angle2: float) -> bool:
    import math
    return math.isclose((angle1 - angle2) % (2 * math.pi), 0, abs_tol=1e-9)
