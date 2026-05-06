def greatest_common_factor_c(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
