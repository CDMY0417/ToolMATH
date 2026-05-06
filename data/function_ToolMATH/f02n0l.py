def factor_quadratic_l(a: int, b: int, c: int):
    for i in range(-abs(c), abs(c) + 1):
        for j in range(-abs(c), abs(c) + 1):
            if i * j == a * c and i + j == b:
                return (a, i), (1, j)
    return None
