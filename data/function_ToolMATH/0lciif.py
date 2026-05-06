def pattern_repeat_modulo_sum(pattern: list[int], repeats: int, mod: int) -> int:
    pattern_sum = sum(pattern) % mod
    total_sum = (pattern_sum * repeats) % mod
    return total_sum
