def sum_of_residues_a(n: int, m: int):
    full_sets = n // m
    remainder_sum = sum(range(1, n % m + 1))
    full_set_sum = sum(range(1, m)) * full_sets
    return (full_set_sum + remainder_sum) % m
