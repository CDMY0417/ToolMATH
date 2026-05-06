def circumference_of_latitude_circle(radius: float, latitude_deg: float) -> float:
    import math
    latitude_rad = math.radians(latitude_deg)
    effective_radius = radius * math.cos(latitude_rad)
    return 2 * math.pi * effective_radius
