def is_valid_triangle_a(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a
