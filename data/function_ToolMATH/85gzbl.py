def chinese_remainder_theorem_two_moduli(a: int, m: int, b: int, n: int) -> int:
    x = a
    while x % n != b:
        x += m
    return x
