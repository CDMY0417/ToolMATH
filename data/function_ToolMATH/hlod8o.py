def sum_of_consecutive_integers_modulo(first_value: int, k: int, m: int) -> int:
    residues = [((first_value + i) % m) for i in range(k)]
    return sum(residues) % m
