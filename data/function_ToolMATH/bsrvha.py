def reduce_exponent_mod_cycle_length(exponent: int, cycle_length: int) -> int:
    return exponent % cycle_length if cycle_length else exponent
