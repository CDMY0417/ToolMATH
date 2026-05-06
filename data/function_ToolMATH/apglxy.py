def scale_inverse_square_force(original_force: float, distance_scale: float) -> float:
    return original_force / (distance_scale ** 2)
