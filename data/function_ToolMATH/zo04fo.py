def cube_root_floor_interval(k: int) -> tuple:
    start = k**3
    end = (k+1)**3 - 1
    return start, end
