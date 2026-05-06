def area_of_sector_a(radius: float, angle_degrees: float) -> float:
    from math import pi
    return (angle_degrees / 360) * pi * (radius ** 2)
