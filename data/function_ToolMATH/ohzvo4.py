def vector_difference_magnitude(magnitude_a: float, magnitude_b: float, dot_ab: float) -> float:
    square_magnitude = magnitude_a**2 - 2 * dot_ab + magnitude_b**2
    return square_magnitude ** 0.5
