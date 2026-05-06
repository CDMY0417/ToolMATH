def greatest_common_divisor_b(a: int, b: int):
    while b:
        a, b = b, a % b
    return a
