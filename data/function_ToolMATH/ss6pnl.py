def mid_point(point1: tuple[float, ...], point2: tuple[float, ...]) -> tuple[float, ...]:
    return tuple((x + y) / 2 for x, y in zip(point1, point2))
