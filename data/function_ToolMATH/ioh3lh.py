def is_valid_triangle_side_lengths(a: float, b: float, c: float) -> bool:
    return (a < b + c) and (b < a + c) and (c < a + b)
