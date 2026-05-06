def triangle_inequality_check(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a
