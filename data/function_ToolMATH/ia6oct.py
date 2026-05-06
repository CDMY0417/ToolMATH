def cosine_from_half_angle_tangent(tan_half_angle: float) -> float:
    x = tan_half_angle
    return (1 - x**2) / (1 + x**2)
