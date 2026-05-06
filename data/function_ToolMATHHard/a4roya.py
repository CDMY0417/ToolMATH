import math

def cos_angle_sum_degrees(deg_a: float, deg_b: float):
    'Compute cos(deg_a + deg_b) with degrees input.'
    a = math.radians(deg_a)
    b = math.radians(deg_b)
    return math.cos(a + b)
