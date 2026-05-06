def addition_is_multiple_of_2pi(angle1: float, angle2: float) -> bool:
    return (angle1 + angle2) % (2 * 3.141592653589793) == 0
