def greatest_common_divisor_k(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
