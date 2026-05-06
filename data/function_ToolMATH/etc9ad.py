def euclidean_distance_3d(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> float:
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)**0.5
