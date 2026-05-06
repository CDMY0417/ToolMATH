def point_on_line_segment(start: tuple, end: tuple, fraction: float) -> tuple:
    x = start[0] + fraction * (end[0] - start[0])
    y = start[1] + fraction * (end[1] - start[1])
    return (x, y)
