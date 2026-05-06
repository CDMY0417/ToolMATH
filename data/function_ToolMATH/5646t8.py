def find_integer_satisfying_modular_condition(multiplier: int, target_remainder: int, mod_value: int, range_end: int) -> int:
    for n in range(range_end):
        if (multiplier * n) % mod_value == target_remainder:
            return n
    return -1
