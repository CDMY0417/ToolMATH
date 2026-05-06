def greatest_common_divisor_d(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
