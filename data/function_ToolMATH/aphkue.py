def modular_multiplicative_inverse(a: int, mod: int) -> int:
    t, new_t = 0, 1
    r, new_r = mod, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if t < 0:
        t = t + mod
    return t
