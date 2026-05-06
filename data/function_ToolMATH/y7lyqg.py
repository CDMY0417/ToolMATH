def calculate_square_vertices(center: tuple, side_length: float):
    cx, cy = center
    half_side = side_length / 2
    vertices = [
        (cx - half_side, cy - half_side),
        (cx - half_side, cy + half_side),
        (cx + half_side, cy + half_side),
        (cx + half_side, cy - half_side)
    ]
    return vertices
