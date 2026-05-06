def distance_between_points_j(point1: tuple[int, int], point2: tuple[int, int]) -> tuple[int, int]:
    x1, y1 = point1
    x2, y2 = point2
    return abs(x2 - x1), abs(y2 - y1)
