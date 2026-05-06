def ratio_of_areas(side_length: float, radius: float) -> float:
    area_square = side_length ** 2
    area_circle = 3.141592653589793 * radius ** 2
    return area_square / area_circle
