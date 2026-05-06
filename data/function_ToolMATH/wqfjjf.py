def midpoint_of_segment_n(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    x_mid = (point1[0] + point2[0]) / 2
    y_mid = (point1[1] + point2[1]) / 2
    return (x_mid, y_mid)
