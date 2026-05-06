def scale_triangle_sides_b(sides: list[float], smallest_side_new: float) -> list[float]:
    scale_factor = smallest_side_new / min(sides)
    return [side * scale_factor for side in sides]
