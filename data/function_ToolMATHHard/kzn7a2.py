import math

def angle_between_2d_vectors_degrees(v1, v2):
    'Return the angle between two 2D vectors in degrees.'
    dot = v1[0]*v2[0] + v1[1]*v2[1]
    m1 = math.hypot(v1[0], v1[1])
    m2 = math.hypot(v2[0], v2[1])
    if m1 == 0 or m2 == 0:
        raise ValueError('vectors must be nonzero')
    cosv = max(-1.0, min(1.0, dot/(m1*m2)))
    return math.degrees(math.acos(cosv))
