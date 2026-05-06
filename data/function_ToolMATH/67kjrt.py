def calculate_distance_between_points(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
