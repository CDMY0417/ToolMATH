import math

def rotate_around_point(x: float, y: float, center_x: float, center_y: float, angle: float):
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)
    x -= center_x
    y -= center_y
    x_new = x * cos_a + y * sin_a
    y_new = -x * sin_a + y * cos_a
    return (x_new + center_x, y_new + center_y)
