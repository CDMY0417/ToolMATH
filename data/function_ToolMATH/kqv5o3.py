def line_intersection_with_x_axis(point1: tuple, point2: tuple):
    x1, y1 = point1
    x2, y2 = point2
    if y1 == y2:
        return None  # Line is parallel to x-axis
    x_intersection = x1 - (x2 - x1) * y1 / (y2 - y1)
    return (x_intersection, 0)
