def max_floor_value(bound: int) -> int:
    a = 0
    while (a + 1) ** 2 < bound:
        a += 1
    return a
