def solve_congruences(a1: int, m1: int, a2: int, m2: int) -> int:
    k = 0
    while (a1 + m1 * k) % m2 != a2:
        k += 1
    n = a1 + m1 * k
    return n
