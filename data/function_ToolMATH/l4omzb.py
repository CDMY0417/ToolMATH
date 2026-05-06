def distance(point1: tuple, point2: tuple) -> float:
    return sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)) ** 0.5
