def rotate_point_180_deg(point: tuple, center: tuple) -> tuple:
    new_x = 2*center[0] - point[0]
    new_y = 2*center[1] - point[1]
    return (new_x, new_y)
