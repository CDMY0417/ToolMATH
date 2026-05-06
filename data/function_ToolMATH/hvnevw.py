def distance_between_points_l(p1: tuple[float, float], p2: tuple[float, float]) -> float:
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
