def smallest_positive_mod_multiple(a: int, m: int) -> int:
    n = (-a) % m
    return n if n > 0 else n + m
