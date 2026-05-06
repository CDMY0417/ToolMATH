def line_parameterization(point: tuple[float, float, float], direction: tuple[float, float, float], t: float) -> tuple[float, float, float]:
    x = point[0] + direction[0] * t
    y = point[1] + direction[1] * t
    z = point[2] + direction[2] * t
    return (x, y, z)
