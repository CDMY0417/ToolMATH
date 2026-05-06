def count_congruent_numbers_a(congruent_number: int, modulus: int, limit: int) -> int:
    max_n = (limit - congruent_number) // modulus
    return max_n + 1
