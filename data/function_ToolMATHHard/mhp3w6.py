import math

def clockwise_rotation_angle_degrees(vx: float, vy: float, vpx: float, vpy: float):
    """Return clockwise angle (0,360)."""
    a1 = math.atan2(vy, vx)
    a2 = math.atan2(vpy, vpx)
    # clockwise angle = (a1 - a2) mod 2pi
    ang = (a1 - a2) % (2*math.pi)
    return ang * 180.0 / math.pi
