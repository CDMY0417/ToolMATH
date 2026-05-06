def matrix_self_inverse(a: float, b: float, c: float, d: float) -> bool:
    return (a ** 2 + b * c == 1) and (b * d + a * c == 0) and (c * a + d * b == 0) and (d ** 2 + b * c == 1)
