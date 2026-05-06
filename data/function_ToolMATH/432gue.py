def is_midpoint(mid: tuple, start: tuple, end: tuple) -> bool:
    return (mid[0] == (start[0] + end[0]) / 2) and (mid[1] == (start[1] + end[1]) / 2)
