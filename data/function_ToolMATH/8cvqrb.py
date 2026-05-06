def area_of_circles(radii: list[float]) -> float:
    from math import pi
    return pi * sum(radius ** 2 for radius in radii)
