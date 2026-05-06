def calculate_cos_from_sin(sin_value: float):
    cos_squared = 1 - sin_value**2
    cos_angle_pos = cos_squared**0.5
    cos_angle_neg = -cos_squared**0.5
    return cos_angle_pos, cos_angle_neg
