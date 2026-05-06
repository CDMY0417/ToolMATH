def factor_quadratic_ar(b: int, c: int):
    for m in range(-abs(c), abs(c) + 1):
        for n in range(-abs(c), abs(c) + 1):
            if m + n == b and m * n == c:
                return m, n
    return None
