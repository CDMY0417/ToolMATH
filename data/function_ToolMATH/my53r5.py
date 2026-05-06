def solve_congruences_a(a1: int, m1: int, a2: int, m2: int) -> int:
    from sympy import mod_inverse
    M = m1 * m2
    m1_inv = mod_inverse(m1, m2)
    m2_inv = mod_inverse(m2, m1)
    x = (a1 * m2 * m2_inv + a2 * m1 * m1_inv) % M
    return x
