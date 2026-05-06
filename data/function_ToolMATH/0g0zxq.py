def fraction_of_square(triangle_area: float, square_side_length: float) -> float:
    total_area = square_side_length ** 2
    shaded_area = total_area - triangle_area
    return shaded_area / total_area
