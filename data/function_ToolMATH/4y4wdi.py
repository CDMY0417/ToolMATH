def modular_inverse_c(a: int, m: int):
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        return None  # a is not invertible
    if t < 0:
        t = t + m
    return t
