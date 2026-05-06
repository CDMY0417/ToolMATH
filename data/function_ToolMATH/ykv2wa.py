def convert_line_to_slope_intercept(a: int, b: int, c: int) -> float:
    # Rewrite equation ax + by = c as by = -ax + c
    # Then y = (-a/b)x + c/b
    return -a / b
