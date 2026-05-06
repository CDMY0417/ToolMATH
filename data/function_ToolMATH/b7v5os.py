def chinese_remainder_theorem(a1: int, n1: int, a2: int, n2: int) -> int:
    n = n1 * n2
    m1 = n // n1
    m2 = n // n2
    inv1 = pow(m1, -1, n1)
    inv2 = pow(m2, -1, n2)
    return (a1 * m1 * inv1 + a2 * m2 * inv2) % n
