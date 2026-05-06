def factor_quadratic_h(b: int, c: int):
    m = -b // 2
    n = m
    if m * n != c:
        m += 1
        n -= 1
    return (m, n) if m * n == c else None
