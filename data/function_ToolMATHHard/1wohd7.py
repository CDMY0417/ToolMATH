import math

def angle_between_vectors_degrees(v1, v2):
    """Return angle in degrees between v1 and v2."""
    dot = sum(a*b for a,b in zip(v1,v2))
    n1 = math.sqrt(sum(a*a for a in v1))
    n2 = math.sqrt(sum(b*b for b in v2))
    cosv = dot/(n1*n2)
    # clamp
    cosv = max(-1.0, min(1.0, cosv))
    return math.degrees(math.acos(cosv))
