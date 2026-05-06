def sum_circle_areas(radii: list[float]) -> float:
    from math import pi
    return sum(pi * radius**2 for radius in radii)
