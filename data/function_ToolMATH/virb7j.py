def cylinder_volume_e(diameter: float, height: float) -> float:
    import math
    radius = diameter / 2
    return math.pi * (radius ** 2) * height
