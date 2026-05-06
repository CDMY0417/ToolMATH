def cube_root_bounds(num: int) -> tuple:
    n = 0
    while (n + 1) ** 3 <= num:
        n += 1
    return n, n + 1
