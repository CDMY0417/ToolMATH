def cylinder_surface_area_a(height: float, radius: float) -> float:
    from math import pi
    circle_area = 2 * pi * radius**2
    lateral_area = 2 * pi * radius * height
    return circle_area + lateral_area
