def greatest_common_divisor_h(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a
