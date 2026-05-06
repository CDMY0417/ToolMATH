def find_modular_cycle(base: int, modulus: int) -> int:
    result = base % modulus
    for exponent in range(1, modulus):
        result = (result * base) % modulus
        if result == 1:
            return exponent
    return modulus
