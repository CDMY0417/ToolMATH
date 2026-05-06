def direction_vector(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> tuple[float, float, float]:
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    dz = point2[2] - point1[2]
    return (dx, dy, dz)
