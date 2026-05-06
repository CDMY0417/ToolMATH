def find_smallest_n_greater_than(b_mod: int, period: int, threshold: int) -> int:
    t = 0
    n = b_mod + period * t
    while n <= threshold:
        t += 1
        n = b_mod + period * t
    return n
