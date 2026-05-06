def greatest_common_divisor_t(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return abs(x)
