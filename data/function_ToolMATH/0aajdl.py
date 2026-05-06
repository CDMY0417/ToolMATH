def distance_between_points(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
