def euclidean_distance_2d(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    from math import sqrt
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
