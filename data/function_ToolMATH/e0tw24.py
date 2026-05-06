def greatest_common_divisor_x(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x
