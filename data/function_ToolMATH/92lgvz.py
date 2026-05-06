def parametrized_line_point(origin: tuple, direction: tuple, t: float):
    x = origin[0] + t * direction[0]
    y = origin[1] + t * direction[1]
    return (x, y)
