def check_trigonometric_identity(sin_x: float, cos_x: float) -> bool:
    return abs(sin_x**2 + cos_x**2 - 1) < 1e-9
