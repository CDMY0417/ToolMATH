def equivalent_positive_residue(residue: int, modulus: int) -> int:
    return (residue % modulus + modulus) % modulus
