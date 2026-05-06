def smallest_n_for_power_condition(limit: int) -> int:
    n = 0
    while 2**(2**(n + 1)) < limit:
        n += 1
    return n
