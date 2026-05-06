def count_integers_in_open_interval(a: float, b: float) -> int:
    return len([x for x in range(int(a) + 1, int(b)) if a < x < b])
