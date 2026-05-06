def modular_inverse_e(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return None
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if a != 1:
        return None
    return x1 + m0 if x1 < 0 else x1
