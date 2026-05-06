import math

def cos_angle_between_linear_combinations(norm_u: float, norm_v: float, dot_uv: float):
    dot = 2*norm_u*norm_u + dot_uv - norm_v*norm_v
    norm1 = math.sqrt(norm_u*norm_u + norm_v*norm_v + 2*dot_uv)
    norm2 = math.sqrt(4*norm_u*norm_u + norm_v*norm_v - 4*dot_uv)
    return dot / (norm1*norm2)
