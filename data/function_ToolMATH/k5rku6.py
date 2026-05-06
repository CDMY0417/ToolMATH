def greatest_common_divisor_u(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a
