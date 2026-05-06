def find_number_with_modulo_conditions(a1: int, m1: int, a2: int, m2: int) -> int:
    n = 0
    while True:
        a = a1 + m1 * n
        if a % m2 == a2:
            return a
        n += 1
