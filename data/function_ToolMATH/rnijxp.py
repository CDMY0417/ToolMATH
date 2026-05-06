def volume_of_square_pyramid(base_edge: float, height: float) -> float:
    base_area = base_edge ** 2
    volume = base_area * height / 3
    return volume
