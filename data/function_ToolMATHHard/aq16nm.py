import math

def cot_degrees(angle_deg):
    rad = math.radians(angle_deg)
    s = math.sin(rad)
    c = math.cos(rad)
    if abs(s) < 1e-12:
        raise ValueError('Cotangent undefined')
    val = c / s
    if abs(val) < 1e-10:
        return 0
    return val
