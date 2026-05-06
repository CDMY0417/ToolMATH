def rotate_point_90_counterclockwise(px: int, py: int, qx: int, qy: int):
    new_x = qx - (py - qy)
    new_y = qy + (px - qx)
    return new_x, new_y
