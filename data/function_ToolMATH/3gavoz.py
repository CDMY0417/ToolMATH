def cos_sin_sum_to_zero(angles: list[float]) -> bool:
    import math
    cos_sum = sum(math.cos(a) for a in angles)
    sin_sum = sum(math.sin(a) for a in angles)
    return cos_sum == 0 and sin_sum == 0
