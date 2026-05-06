def midpoint_c(point1: tuple, point2: tuple):
    return tuple((p1 + p2) / 2 for p1, p2 in zip(point1, point2))
