def calculate_squared_distance(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> float:
    return (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2
