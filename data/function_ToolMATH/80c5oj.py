def greatest_common_factor_q(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
