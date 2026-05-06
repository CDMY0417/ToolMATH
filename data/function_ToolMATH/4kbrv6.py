def triangle_inequality_b(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a
