def calculate_similar_side_ratio(side_length_known_triangle: float, side_ratio_known_triangle: float, side_ratio_other_triangle: float):
    return side_length_known_triangle * (side_ratio_other_triangle / side_ratio_known_triangle)
