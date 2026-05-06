def greatest_common_factor_k(a: int, b: int):
    while b != 0:
        a, b = b, a % b
    return a
