def largest_integer_congruent_to_mod(remainder: int, modulus: int, limit: int) -> int:
    n = (limit - 1 - remainder) // modulus
    return modulus * n + remainder
