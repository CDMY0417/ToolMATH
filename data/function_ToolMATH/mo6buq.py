def greatest_common_divisor_v(a: int, b: int):
    while b:
        a, b = b, a % b
    return abs(a)
