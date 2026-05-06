def distance_between_points_av(point1: tuple[int, int], point2: tuple[int, int]) -> tuple[int, int]:
    return abs(point2[0] - point1[0]), abs(point2[1] - point1[1])
