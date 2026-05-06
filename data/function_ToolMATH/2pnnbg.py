import math

def triangle_area_az(a: float, b: float, angle_deg: float):
    angle_rad = math.radians(angle_deg)
    return 0.5 * a * b * math.sin(angle_rad)
