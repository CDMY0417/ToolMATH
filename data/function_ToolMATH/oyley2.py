def combine_linear_congruences(a1: int, b1: int, m1: int, a2: int, b2: int, m2: int) -> int:
    for n in range(m1 * m2):
        if (a1 * n + b1) % m1 == 0 and (a2 * n + b2) % m2 == 0:
            return n
    return None
