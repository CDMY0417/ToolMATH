def reflect_in_xy_plane(point: tuple[float, float, float]) -> tuple[float, float, float]:
    x, y, z = point
    return (x, y, -z)
