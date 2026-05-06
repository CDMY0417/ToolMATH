import math

def sum_reciprocals_coplanar_points(b, c):
    if b == 1 or c == 1 or b * c == 1:
        raise ValueError('Invalid parameters')
    a = (b + c - 2) / (b * c - 1)
    return 1/(1 - a) + 1/(1 - b) + 1/(1 - c)
