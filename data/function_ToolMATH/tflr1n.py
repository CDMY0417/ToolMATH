def calculate_sine_from_cosine(cos_x: float, quadrant: int) -> float:
    sin_square_x = 1 - cos_x**2
    sin_x = (-1 if quadrant in [3, 4] else 1) * (sin_square_x**0.5)
    return sin_x
