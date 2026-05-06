def is_point_in_first_quadrant(x: float, y: float, constraint: float) -> bool:
    if x >= 0 and y >= 0:
        if y >= x:
            return 2 * y <= constraint
        else:
            return 2 * x <= constraint
    return False
