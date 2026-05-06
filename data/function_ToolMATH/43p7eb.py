def greatest_common_divisor_c(x: int, y: int):
    while y:
        x, y = y, x % y
    return x
