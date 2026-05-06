def largest_congruent_number(congruent_number: int, modulus: int, limit: int) -> int:
    max_n = (limit - congruent_number) // modulus
    return congruent_number + modulus * max_n
