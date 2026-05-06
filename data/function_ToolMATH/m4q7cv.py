def calculate_line_segment_length(point1: tuple, point2: tuple) -> float:
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
