def sector_area_a(radius: float, angle_deg: float) -> float:
    import math
    return (angle_deg / 360) * math.pi * (radius ** 2)
