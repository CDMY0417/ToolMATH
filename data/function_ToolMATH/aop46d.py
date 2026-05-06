def valid_triangle_side(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a
