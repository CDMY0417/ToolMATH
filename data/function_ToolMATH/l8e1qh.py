def trig_identity_transformation(theta: float, is_cosine: bool):
    import math
    if is_cosine:
        return math.sin(theta) ** 2
    else:
        return math.cos(theta) ** 2
