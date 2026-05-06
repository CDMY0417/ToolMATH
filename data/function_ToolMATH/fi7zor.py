def symmetry_check(point1: tuple, point2: tuple, axis: str) -> bool:
    if axis == 'x':
        return point1 == (point2[0], -point2[1])
    elif axis == 'y':
        return point1 == (-point2[0], point2[1])
    return False
