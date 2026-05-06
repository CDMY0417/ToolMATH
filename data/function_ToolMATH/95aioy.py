def calculate_modular_sequence_count(max_value: int, remainder: int, modulus: int) -> int:
    max_k = (max_value - remainder) // modulus
    return max_k + 1
