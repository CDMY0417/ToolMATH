def modular_exponentiation_k(base: int, power: int, mod: int) -> int:
    result = 1
    base = base % mod
    while power > 0:
        if (power % 2) == 1:
            result = (result * base) % mod
        power = power // 2
        base = (base * base) % mod
    return result
