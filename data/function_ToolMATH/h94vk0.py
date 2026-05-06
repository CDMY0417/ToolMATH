def find_number_with_modular_conditions(mod1: int, rem1: int, mod2: int, rem2: int, limit: int) -> int:
    current = rem1
    while current < limit:
        if current % mod2 == rem2:
            return current
        current += mod1
    return -1
