def sum_of_residues(n: int, modulo: int) -> int:
    full_sets = n // modulo
    remainder = n % modulo
    sum_full_sets = full_sets * sum(range(modulo)) % modulo
    sum_remainder = sum(range(1, remainder + 1)) % modulo
    return (sum_full_sets + sum_remainder) % modulo
