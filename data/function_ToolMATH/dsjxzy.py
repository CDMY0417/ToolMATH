def translate_y_direction(point: tuple, units: int):
    x, y, z = point
    return (x, y + units, z)
