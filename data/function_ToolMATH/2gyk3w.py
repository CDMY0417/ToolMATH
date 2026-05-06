def modular_inverse_b(num: int, mod: int):
    for inv in range(1, mod):
        if (num * inv) % mod == 1:
            return inv
    return None
