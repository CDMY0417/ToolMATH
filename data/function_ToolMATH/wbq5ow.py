def modular_exponentiation_r(base: int, exp: int, mod: int):
    if exp == 0:
        return 1
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result
