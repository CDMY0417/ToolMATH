def area_of_sector(radius: float, angle_degrees: float) -> float:
    angle_radians = angle_degrees * (3.141592653589793 / 180)
    return 0.5 * radius * radius * angle_radians
