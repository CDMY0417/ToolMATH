def congruence_sequence_count(a: int, b: int, limit: int) -> int:
    k_max = (limit - a - 1) // b
    return k_max + 1
