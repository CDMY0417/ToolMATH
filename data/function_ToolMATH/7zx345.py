def multiply_congruence(a: int, b: int, mod: int, mult: int):
    """
    Multiply both sides of the congruence a ≡ b (mod mod) by a constant mult.
    Returns the new left and right sides.
    """
    new_a = a * mult
    new_b = b * mult
    return new_a, new_b
