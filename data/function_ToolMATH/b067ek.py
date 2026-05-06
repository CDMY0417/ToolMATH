def parameterize_line(point: tuple, direction: tuple, t: float):
    return tuple(p + t * d for p, d in zip(point, direction))
