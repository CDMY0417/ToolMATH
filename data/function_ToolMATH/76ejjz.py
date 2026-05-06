def add_congruence_constants(x_coeff: int, constant: int, addend: int, modulus: int):
    new_constant = (constant + addend) % modulus
    return x_coeff, new_constant
