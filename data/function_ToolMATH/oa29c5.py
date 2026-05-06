def cube_less_than(limit: int) -> int:
    n = 1
    while (n + 1) ** 3 < limit:
        n += 1
    return n
