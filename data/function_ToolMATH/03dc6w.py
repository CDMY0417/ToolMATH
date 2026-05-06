def greatest_common_divisor_r(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
