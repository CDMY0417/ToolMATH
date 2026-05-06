def similar_cone_height(small_radius: float, large_radius: float, truncated_height: float) -> float:
    return truncated_height * (small_radius / (large_radius - small_radius))
