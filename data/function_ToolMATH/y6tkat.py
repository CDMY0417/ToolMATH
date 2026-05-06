def greatest_common_factor_r(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
