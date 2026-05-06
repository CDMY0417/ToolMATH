def greatest_common_divisor_o(a: int, b: int):
    while b:
        a, b = b, a % b
    return a
