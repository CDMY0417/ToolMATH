def greatest_common_divisor_g(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a
