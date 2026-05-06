import math

def rotate_point_b(point: tuple[float, float], angle_deg: float):
    angle_rad = math.radians(angle_deg)
    x, y = point
    x_new = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    y_new = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return (x_new, y_new)
