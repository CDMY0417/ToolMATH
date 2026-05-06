def find_midpoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    mx = (point1[0] + point2[0]) / 2
    my = (point1[1] + point2[1]) / 2
    return (mx, my)
