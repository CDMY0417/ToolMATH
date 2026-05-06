def circle_area_greater_radius(max_area: float) -> int:
    from math import sqrt
    max_radius_squared = max_area / 3.14159
    max_radius = int(sqrt(max_radius_squared))
    return max_radius
