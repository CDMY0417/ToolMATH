def smallest_integer_congruent_to_modulo(num_digits: int, remainder: int, modulo: int) -> int:
    lower_bound = 10**(num_digits - 1)
    k = (lower_bound - remainder + modulo - 1) // modulo
    return modulo * k + remainder
