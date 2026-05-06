def modular_inverse_s(number: int, modulus: int):
    m0, x0, x1 = modulus, 0, 1
    a = number
    while a > 1:
        q = a // modulus
        modulus, a = a % modulus, modulus
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1
