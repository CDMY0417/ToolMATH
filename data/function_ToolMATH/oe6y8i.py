def invert_modulo(value: int, mod: int) -> int:
    for x in range(1, mod):
        if (value * x) % mod == 1:
            return x
    return None
