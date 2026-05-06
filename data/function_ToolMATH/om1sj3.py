def chinese_remainder_theorem_two_moduli_a(a1: int, n1: int, a2: int, n2: int) -> int:
    for x in range(n1):
        if x * n2 % n1 == (a1 - a2) % n1:
            return (x * n2 + a2) % (n1 * n2)
    return None
