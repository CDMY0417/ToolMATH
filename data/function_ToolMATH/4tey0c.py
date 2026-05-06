def solve_linear_congruence_a(a: int, b: int, c: int, modulus: int):
    a = a % modulus
    b = b % modulus
    c = c % modulus
    x_coeff = (a % modulus)
    constant = (c - b) % modulus
    return x_coeff, constant
