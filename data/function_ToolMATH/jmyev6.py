def midpoint_coordinates_e(x_coords: list[float]):
    n = len(x_coords)
    return [(x_coords[i] + x_coords[(i + 1) % n]) / 2 for i in range(n)]
