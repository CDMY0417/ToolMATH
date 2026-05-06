def exponential_to_rectangular(angle_radians: float):
    from math import cos, sin
    return cos(angle_radians) + 1j * sin(angle_radians)
