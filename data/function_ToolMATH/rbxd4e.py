def area_of_similar_triangle_a(original_area: float, side_ratio: float) -> float:
    area_ratio = side_ratio ** 2
    return original_area * area_ratio
