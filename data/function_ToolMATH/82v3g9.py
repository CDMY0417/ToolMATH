def line_segment_length(point1: tuple, point2: tuple) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
