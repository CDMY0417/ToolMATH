def greatest_common_divisor_m(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
