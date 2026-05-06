def similar_triangles_ratio_c(side_1: float, side_2: float, reference_side: float) -> float:
    ratio = side_1 / side_2
    corresponding_side = reference_side * ratio
    return corresponding_side
