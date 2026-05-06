import math

def principal_arccos_of_cos(x: float):
    # Return arccos(cos x) in [0, pi]
    twopi = 2*math.pi
    r = x % twopi
    if r <= math.pi:
        return r
    return twopi - r
