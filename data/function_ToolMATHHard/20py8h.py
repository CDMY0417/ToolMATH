import math

def angle_between_vectors_deg(v1, v2):
    if len(v1) != len(v2):
        raise ValueError('Vectors must have same dimension')
    dot = sum(a*b for a,b in zip(v1,v2))
    norm1 = math.sqrt(sum(a*a for a in v1))
    norm2 = math.sqrt(sum(b*b for b in v2))
    if norm1 == 0 or norm2 == 0:
        raise ValueError('Zero vector')
    cos_val = dot / (norm1 * norm2)
    cos_val = max(-1.0, min(1.0, cos_val))
    return math.degrees(math.acos(cos_val))
