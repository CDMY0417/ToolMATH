import math

def rotate_point_on_circle(angle_deg: float):
    rad = math.radians(angle_deg)
    return (math.cos(rad), math.sin(rad))
