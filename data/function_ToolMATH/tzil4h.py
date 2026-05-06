def is_non_degenerate_triangle(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a
