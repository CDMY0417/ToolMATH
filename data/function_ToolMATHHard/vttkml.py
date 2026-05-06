import math

def max_scalar_triple_with_unit_vector(b, c):
    # maximum of a · (b x c) with ||a||=1 is ||b x c||
    bx, by, bz = b
    cx, cy, cz = c
    cross = [by*cz - bz*cy, bz*cx - bx*cz, bx*cy - by*cx]
    return math.sqrt(sum(v*v for v in cross))
