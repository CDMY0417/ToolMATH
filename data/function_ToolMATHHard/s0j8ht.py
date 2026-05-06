import math

def real_part_from_modulus_and_imag(modulus: float, imag: float):
    """Return positive real part from modulus and imaginary part."""
    if modulus <= 0:
        raise ValueError("modulus must be positive.")
    val = modulus*modulus - imag*imag
    if val < 0:
        raise ValueError("No real solution.")
    return math.sqrt(val)
