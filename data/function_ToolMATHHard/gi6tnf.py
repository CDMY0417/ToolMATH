import math

def rotate_point_2d_degrees(point, deg: float):
    x,y = point
    th = math.radians(deg)
    c = math.cos(th); s = math.sin(th)
    return [c*x - s*y, s*x + c*y]
